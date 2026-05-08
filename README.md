# Bynder Customer Support Agent

An agentic RAG system that answers questions about Bynder's digital asset management platform, grounded in ~330 official support articles.

## Architecture

```
User Question
     |
     v
[Agentic Loop - gpt-4.1-mini]
     |
     |--- decides to search ---> search_knowledge_base(query)
     |                                    |
     |                                    v
     |                           ChromaDB vector store
     |                           (text-embedding-3-small)
     |                                    |
     |<--- retrieved articles -----------/
     |
     |--- (may search again with different query) ----> ...
     |
     v
Streamed answer with citations
     |
     v
Chainlit UI with tool-call transparency
```

The agent uses OpenAI function calling to decide when and what to search. The LLM reasons about the query, formulates its own search terms, and can search multiple times for complex questions if needed. This also handles follow-up questions naturally, the agent sees the conversation history and reformulates queries to resolve references.

## Engineering Decisions


### Chunking Strategy

Two-stage chunking:
1. **MarkdownHeaderTextSplitter**: splits on H1/H2/H3 headers, preserving document structure
2. **RecursiveCharacterTextSplitter**: further splits to 1000 chars with 200 char overlap

Each chunk is prefixed with `Title > Section` to enrich the embedding with structural context.

### Model Choices

- **gpt-4.1-mini** for the agent. It balances quality and cost for reasoning + answering
- **text-embedding-3-small** for embeddings. Cost-effective for this corpus size (~330 articles)

### Retrieval Design

- Fetches 3x candidates, then deduplicates by article (max 3 chunks per article) to ensure source diversity
- Score threshold (0.35) filters low-relevance noise
- Content based chunk IDs (hash of file_id + section + text) for idempotent re ingestion

## Setup

### Prerequisites

- Python 3.13+
- [uv](https://docs.astral.sh/uv/) package manager
- OpenAI API key

### Install & Run

```bash
# Install dependencies
uv sync

# Set up environment
cp .env.example .env
# Edit .env with your OpenAI API key

# Ingest knowledge base (first time)
uv run python ingest.py

# Start the app
uv run chainlit run app.py
```

### Re-ingestion

```bash
# Incremental (only new files)
uv run python ingest.py

# Full rebuild
uv run python ingest.py --force
```

## Evaluation

Run the 9 sample test questions to validate the agent:

```bash
# Run all questions
uv run python evaluate.py

# Run a specific question
uv run python evaluate.py --question 3
```

The script runs each question through the agent, displays tool calls and answers, and checks for expected keywords in responses.

## What I'd Improve with More Time

- **Hybrid search**: combine semantic search with BM25/keyword search for better recall on exact terms
- **Reranking**: add a cross-encoder reranker after initial retrieval for more precise context
- **Adaptive model routing**: use a cheaper model for simple lookups, stronger model for complex synthesis
- **LLM-as-judge evaluation**: automated answer quality scoring beyond keyword matching
- **Caching**: cache frequent queries to reduce latency and API costs
- **Observability**: add tracing (e.g., OpenTelemetry) for debugging retrieval quality in production
- **Multi-modal**: accept screenshots of issues via Chainlit's file upload
