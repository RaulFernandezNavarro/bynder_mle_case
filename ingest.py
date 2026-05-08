import argparse
import hashlib
import logging
import os
import re

import chromadb
from chromadb.utils.embedding_functions import OpenAIEmbeddingFunction
from dotenv import load_dotenv
from langchain_text_splitters import (
    MarkdownHeaderTextSplitter,
    RecursiveCharacterTextSplitter,
)
from tqdm import tqdm
from tqdm.contrib.logging import logging_redirect_tqdm

from config import (
    ARTICLES_DIR,
    CHUNK_OVERLAP,
    CHUNK_SIZE,
    COLLECTION_NAME,
    EMBEDDING_MODEL,
    VECTOR_STORE_DIR,
)
from logging_config import setup_logging

logger = logging.getLogger(__name__)


class IngestPipeline:
    def __init__(
        self,
        src_path=ARTICLES_DIR,
        dest_path=VECTOR_STORE_DIR,
        collection_name=COLLECTION_NAME,
        embedding_model=EMBEDDING_MODEL,
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
    ):
        self.src_path = src_path
        self.dest_path = dest_path
        self.collection_name = collection_name
        self.embedding_model = embedding_model
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.client = chromadb.PersistentClient(path=self.dest_path)
        self.BATCH_SIZE = 100

    def run(self, force=False):
        # Delete collection if it already exists and force is True
        if force:
            logger.info(
                f"Force is True. Deleting collection '{self.collection_name}' if it exists."
            )
            self.client.delete_collection(self.collection_name)

        embedding_fn = OpenAIEmbeddingFunction(
            api_key=os.environ["OPENAI_API_KEY"],
            model_name=self.embedding_model,
        )
        logger.info(f"Using embedding model: {self.embedding_model}")

        collection = self.client.get_or_create_collection(
            name=self.collection_name,
            embedding_function=embedding_fn,
            metadata={"hnsw:space": "cosine"},
        )

        file_paths = list(self.src_path.glob("*.md"))

        if not force:
            existing_ids = collection.get(include=[])["ids"]
            indexed_file_ids = {cid.split("_")[0] for cid in existing_ids}
            before = len(file_paths)
            file_paths = [p for p in file_paths if p.stem.split("_")[0] not in indexed_file_ids]
            logger.info(f"Found {len(file_paths)} new files to ingest (skipped {before - len(file_paths)} already indexed).")
        else:
            logger.info(f"Found {len(file_paths)} files to ingest.")

        chunks = []
        for path in file_paths:
            logger.debug(f"Processing file: {path}")
            file = self._parse_file(path)
            chunks.extend(self._chunk_file(file))

        logger.info(
            f"Ingesting {len(chunks)} chunks into collection '{self.collection_name}'."
        )
        with logging_redirect_tqdm():
            for batch_start in tqdm(range(0, len(chunks), self.BATCH_SIZE)):
                batch = chunks[batch_start : batch_start + self.BATCH_SIZE]
                ids = [self._chunk_id(chunk) for chunk in batch]
                documents = [chunk["text"] for chunk in batch]
                metadatas = [
                    {
                        "file_id": chunk["file_id"],
                        "title": chunk["title"],
                        "source_url": chunk["source_url"],
                        "section": chunk["section"],
                    }
                    for chunk in batch
                ]
                collection.upsert(ids=ids, documents=documents, metadatas=metadatas)

        logger.info("Ingestion completed.")

    @staticmethod
    def _chunk_id(chunk: dict) -> str:
        content_hash = hashlib.md5(
            f"{chunk['file_id']}_{chunk['section']}_{chunk['text'][:200]}".encode()
        ).hexdigest()[:12]
        return f"{chunk['file_id']}_{content_hash}"

    def _parse_file(self, path):
        content = path.read_text(encoding="utf-8")

        file_id = path.stem.split("_")[0]

        title_match = re.search(r"^# (.+)$", content, re.MULTILINE)
        title = title_match.group(1).strip() if title_match else path.stem

        url_match = re.search(r"\*\*Source URL:\*\*\s*(https?://\S+)", content)
        source_url = url_match.group(1).strip() if url_match else ""

        return {
            "content": content,
            "file_id": file_id,
            "title": title,
            "source_url": source_url,
        }

    def _chunk_file(self, article: dict) -> list[dict]:
        headers_to_split_on = [("#", "h1"), ("##", "h2"), ("###", "h3")]
        md_splitter = MarkdownHeaderTextSplitter(
            headers_to_split_on=headers_to_split_on
        )
        char_splitter = RecursiveCharacterTextSplitter(
            chunk_size=self.chunk_size, chunk_overlap=self.chunk_overlap
        )

        md_chunks = md_splitter.split_text(article["content"])
        final_chunks = char_splitter.split_documents(md_chunks)

        chunks = []
        for doc in final_chunks:
            section = " > ".join(
                filter(
                    None,
                    [
                        doc.metadata.get("h1"),
                        doc.metadata.get("h2"),
                        doc.metadata.get("h3"),
                    ],
                )
            )
            # Prefix chunk text with title + section for richer embeddings TODO: is this needed or does chroma handle it with metadata?
            prefix = article["title"]
            if section:
                prefix = f"{prefix} > {section}"
            text = f"{prefix}\n\n{doc.page_content}"

            chunks.append(
                {
                    "text": text,
                    "file_id": article["file_id"],
                    "title": article["title"],
                    "source_url": article["source_url"],
                    "section": section,
                }
            )

        return chunks


if __name__ == "__main__":
    load_dotenv()
    setup_logging()

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--force", action="store_true", help="Rebuild index from scratch"
    )
    args = parser.parse_args()

    pipeline = IngestPipeline()
    pipeline.run(force=args.force)
