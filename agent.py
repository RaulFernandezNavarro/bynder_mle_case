import logging
import os

from openai import AsyncOpenAI

from config import LLM_MODEL, REWRITE_MODEL
from prompts import REWRITE_PROMPT, SYSTEM_PROMPT
from retriever import Retriever

logger = logging.getLogger(__name__)
client = AsyncOpenAI(api_key=os.environ["OPENAI_API_KEY"])
retriever = Retriever()


def build_context(chunks: list[dict]) -> str:
    parts = ["Support articles:"]
    for chunk in chunks:
        parts.append(f"[{chunk['title']}]\n{chunk['text']}")
    return "\n\n---\n\n".join(parts)


async def rewrite_query(query: str, history: list[dict]) -> str:
    if not history:
        return query

    conversation = "\n".join(
        f"{'User' if m['role'] == 'user' else 'Assistant'}: {m['content']}"
        for m in history
    )

    messages = [
        {
            "role": "user",
            "content": (
                f"Conversation so far:\n{conversation}\n\n"
                f"Latest user message: {query}\n\n"
                "Rewrite the latest user message as a short, standalone search query "
                "that resolves any pronouns or references. Output only the query."
            ),
        }
    ]

    response = await client.chat.completions.create(
        model=REWRITE_MODEL,
        messages=messages,
    )
    rewritten = response.choices[0].message.content.strip()
    logger.debug(f"Query rewrite: '{query}' -> '{rewritten}'")
    return rewritten


def retrieve(search_query: str) -> list[dict]:
    chunks = retriever.search(search_query)
    logger.debug(f"Retrieved {len(chunks)} chunks from vector store")
    return chunks


async def stream_answer(query: str, chunks: list[dict], history: list[dict]):
    context = build_context(chunks) if chunks else ""
    system = SYSTEM_PROMPT.format(context=context)
    messages = [
        {"role": "system", "content": system},
        *history,
        {"role": "user", "content": query},
    ]

    stream = await client.chat.completions.create(
        model=LLM_MODEL, messages=messages, stream=True
    )
    async for chunk in stream:
        delta = chunk.choices[0].delta.content
        if delta:
            yield delta
