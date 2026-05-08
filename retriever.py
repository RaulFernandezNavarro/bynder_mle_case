import logging
import os

import chromadb
from chromadb.utils.embedding_functions import OpenAIEmbeddingFunction

from config import (
    CHUNK_SCORE_THRESHOLD,
    COLLECTION_NAME,
    EMBEDDING_MODEL,
    MAX_CHUNKS_PER_ARTICLE,
    TOP_K,
    VECTOR_STORE_DIR,
)

logger = logging.getLogger(__name__)


class Retriever:
    def __init__(
        self,
        dest_path=VECTOR_STORE_DIR,
        collection_name=COLLECTION_NAME,
        embedding_model=EMBEDDING_MODEL,
        top_k=TOP_K,
        max_chunks_per_article=MAX_CHUNKS_PER_ARTICLE,
    ):
        self.top_k = top_k
        self.max_chunks_per_article = max_chunks_per_article
        embedding_fn = OpenAIEmbeddingFunction(
            api_key=os.environ["OPENAI_API_KEY"],
            model_name=embedding_model,
        )
        client = chromadb.PersistentClient(path=dest_path)
        self.collection = client.get_collection(
            name=collection_name,
            embedding_function=embedding_fn,
        )

    def search(self, query: str) -> list[dict]:
        # Fetch more candidates than needed, then deduplicate by article
        results = self.collection.query(
            query_texts=[query],
            n_results=self.top_k * 3,
            include=["documents", "metadatas", "distances"],
        )

        seen_titles: dict[str, int] = {}
        chunks = []
        for doc, metadata, distance in zip(
            results["documents"][0],
            results["metadatas"][0],
            results["distances"][0],
        ):
            title = metadata["title"]
            count = seen_titles.get(title, 0)
            if count >= self.max_chunks_per_article:
                continue
            seen_titles[title] = count + 1
            chunks.append(
                {
                    "text": doc,
                    "title": title,
                    "source_url": metadata["source_url"],
                    "section": metadata["section"],
                    "score": round(1 - distance, 4),
                }
            )
            if len(chunks) == self.top_k:
                break

        # Delete chunks with less than X score
        chunks = [chunk for chunk in chunks if chunk["score"] >= CHUNK_SCORE_THRESHOLD]
        logger.debug(f"Retrieving the following chunks for query '{query}': {chunks}")

        return chunks
