from pathlib import Path

# Paths
ARTICLES_DIR = Path("MLE_Assignment/bynder_support_md")
VECTOR_STORE_DIR = "vector_store"

# Collection
COLLECTION_NAME = "bynder_support"

# Models
EMBEDDING_MODEL = "text-embedding-3-small"
REWRITE_MODEL = "gpt-4.1-nano"
LLM_MODEL = "gpt-4.1-mini"

# Chunking
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200
CHUNK_SCORE_THRESHOLD = 0.35

# Retrieval
TOP_K = 5
MAX_CHUNKS_PER_ARTICLE = 3
