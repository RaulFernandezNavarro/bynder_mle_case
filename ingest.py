import chromadb
import os
import logging
import re
from langchain.text_splitter import MarkdownHeaderTextSplitter, RecursiveCharacterTextSplitter
from chromadb.utils.embedding_functions import OpenAIEmbeddingFunction
from tqdm import tqdm



logger = logging.getLogger(__name__)

class IngestPipeline:
    def __init__(self, src_path, dest_path, collection_name, embedding_model):
        self.src_path = src_path
        self.dest_path = dest_path
        self.collection_name = collection_name
        self.embedding_model = embedding_model
        self.client = chromadb.PersistentClient(path=self.dest_path)
        self.BATCH_SIZE = 100
        self.CHUNK_SIZE = 600 # TODO: Do these based on data from the docs
        self.CHUNK_OVERLAP = 100

    def run(self, force=False):
        # Delete collection if it already exists and force is True
        if force:
            logger.info(f"Force is True. Deleting collection '{self.collection_name}' if it exists.")
            self.client.delete_collection(self.collection_name)
        
        self.collection = self.client.create_collection(self.collection_name)
        
        # Embedding funciton
        embedding_fn = OpenAIEmbeddingFunction(
            api_key=os.environ["OPENAI_API_KEY"],
            model_name=self.embedding_model,
        )
        logger.info(f"Using embedding model: {self.embedding_model}")
        
        collection = self.client.get_or_create_collection(
            name=self.collection_name,
            embedding_function=embedding_fn,
        )
        
        # TODO: ingest files that are not present in the collection
        file_paths = list(self.src_path.glob("*.md"))
        logger.info(f"Found {len(file_paths)} files to ingest.")
        
        chunks = []
        for path in file_paths:
            logger.debug(f"Processing file: {path}")
            file = self._parse_file(path)
            chunks.extend(self._chunk_file(file))
        
        logger.info(f"Ingesting {len(chunks)} chunks into collection '{self.collection_name}'.")
        for batch_start in tqdm(range(0, len(chunks), self.BATCH_SIZE)):
            batch = chunks[batch_start:batch_start + self.BATCH_SIZE]
            ids=[f"{chunk['file_id']}_{batch_start + batch_index}" for batch_index, chunk in enumerate(batch)]
            documents=[chunk["text"] for chunk in batch]
            metadatas=[
                    {
                        "file_id": chunk["file_id"],
                        "title": chunk["title"],
                        "source_url": chunk["source_url"],
                        "section": chunk["section"],
                    }
                    for chunk in batch
                ]
            collection.add(ids=ids, documents=documents, metadatas=metadatas)

        logger.info("Ingestion completed.")

    def _parse_file(self, path):
        content = path.read_text(encoding="utf-8")

        file_id = path.stem.split("_")[0]

        title_match = re.search(r"^# (.+)$", content, re.MULTILINE)
        title = title_match.group(1).strip() if title_match else path.stem

        url_match = re.search(r"\*\*Source URL:\*\*\s*(https?://\S+)", content)
        source_url = url_match.group(1).strip() if url_match else ""

        return {"content": content, "file_id": file_id, "title": title, "source_url": source_url}
    
    def _chunk_file(self, article: dict) -> list[dict]:
        headers_to_split_on = [("#", "h1"), ("##", "h2"), ("###", "h3")]
        md_splitter = MarkdownHeaderTextSplitter(headers_to_split_on=headers_to_split_on)
        char_splitter = RecursiveCharacterTextSplitter(chunk_size=self.CHUNK_SIZE, chunk_overlap=self.CHUNK_OVERLAP)

        md_chunks = md_splitter.split_text(article["content"])
        final_chunks = char_splitter.split_documents(md_chunks)

        chunks = []
        for doc in final_chunks:
            section = " > ".join(filter(None, [
                doc.metadata.get("h1"),
                doc.metadata.get("h2"),
                doc.metadata.get("h3"),
            ]))
            # Prefix chunk text with title + section for richer embeddings TODO: is this needed or does chroma handle it with metadata?
            prefix = article["title"]
            if section:
                prefix = f"{prefix} > {section}"
            text = f"{prefix}\n\n{doc.page_content}"

            chunks.append({
                "text": text,
                "file_id": article["file_id"],
                "title": article["title"],
                "source_url": article["source_url"],
                "section": section,
            })

        return chunks
