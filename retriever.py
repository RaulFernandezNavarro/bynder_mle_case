import logging
import os
import re

import chromadb
from chromadb.utils.embedding_functions import OpenAIEmbeddingFunction
from rank_bm25 import BM25Okapi

from config import (
    CHUNK_SCORE_THRESHOLD,
    COLLECTION_NAME,
    EMBEDDING_MODEL,
    MAX_CHUNKS_PER_ARTICLE,
    RRF_K,
    TOP_K,
    VECTOR_STORE_DIR,
)

logger = logging.getLogger(__name__)

_TOKENIZE_RE = re.compile(r"\w+")


def _tokenize(text: str) -> list[str]:
    return _TOKENIZE_RE.findall(text.lower())


class Retriever:
    def __init__(
        self,
        dest_path=VECTOR_STORE_DIR,
        collection_name=COLLECTION_NAME,
        embedding_model=EMBEDDING_MODEL,
        top_k=TOP_K,
        max_chunks_per_article=MAX_CHUNKS_PER_ARTICLE,
        rrf_k=RRF_K,
    ):
        self.top_k = top_k
        self.max_chunks_per_article = max_chunks_per_article
        self.rrf_k = rrf_k

        embedding_fn = OpenAIEmbeddingFunction(
            api_key=os.environ["OPENAI_API_KEY"],
            model_name=embedding_model,
        )
        client = chromadb.PersistentClient(path=dest_path)
        self.collection = client.get_collection(
            name=collection_name,
            embedding_function=embedding_fn,
        )

        self._build_bm25_index()

    def _build_bm25_index(self):
        all_docs = self.collection.get(include=["documents", "metadatas"])
        self._bm25_ids = all_docs["ids"]
        self._bm25_docs = all_docs["documents"]
        self._bm25_metadatas = all_docs["metadatas"]

        tokenized = [_tokenize(doc) for doc in self._bm25_docs]
        self._bm25 = BM25Okapi(tokenized)
        logger.info(f"Built BM25 index with {len(self._bm25_ids)} documents")

    def _semantic_search(self, query: str, n: int) -> list[tuple[str, float]]:
        results = self.collection.query(
            query_texts=[query],
            n_results=n,
            include=["distances"],
        )
        ranked = []
        for doc_id, distance in zip(results["ids"][0], results["distances"][0]):
            ranked.append((doc_id, 1 - distance))
        return ranked

    def _bm25_search(self, query: str, n: int) -> list[tuple[str, float]]:
        scores = self._bm25.get_scores(_tokenize(query))
        top_indices = sorted(range(len(scores)), key=lambda i: scores[i], reverse=True)[:n]
        return [(self._bm25_ids[i], scores[i]) for i in top_indices if scores[i] > 0]

    def search(self, query: str) -> list[dict]:
        candidates = self.top_k * 3

        semantic_results = self._semantic_search(query, candidates)
        bm25_results = self._bm25_search(query, candidates)

        # Reciprocal Rank Fusion
        rrf_scores: dict[str, float] = {}
        for rank, (doc_id, _) in enumerate(semantic_results):
            rrf_scores[doc_id] = rrf_scores.get(doc_id, 0) + 1 / (self.rrf_k + rank + 1)
        for rank, (doc_id, _) in enumerate(bm25_results):
            rrf_scores[doc_id] = rrf_scores.get(doc_id, 0) + 1 / (self.rrf_k + rank + 1)

        sorted_ids = sorted(rrf_scores, key=rrf_scores.get, reverse=True)

        id_to_idx = {doc_id: i for i, doc_id in enumerate(self._bm25_ids)}
        semantic_scores = dict(semantic_results)

        seen_titles: dict[str, int] = {}
        chunks = []
        for doc_id in sorted_ids:
            idx = id_to_idx[doc_id]
            metadata = self._bm25_metadatas[idx]
            title = metadata["title"]

            count = seen_titles.get(title, 0)
            if count >= self.max_chunks_per_article:
                continue
            seen_titles[title] = count + 1

            similarity = semantic_scores.get(doc_id)
            if similarity is not None and similarity < CHUNK_SCORE_THRESHOLD:
                continue

            chunks.append({
                "text": self._bm25_docs[idx],
                "title": title,
                "source_url": metadata["source_url"],
                "section": metadata["section"],
                "score": round(rrf_scores[doc_id], 4),
            })

            if len(chunks) == self.top_k:
                break

        logger.debug(f"Hybrid search for '{query}': {len(chunks)} chunks returned")
        return chunks
