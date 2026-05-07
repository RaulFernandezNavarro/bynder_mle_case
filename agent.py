import os
import logging
from openai import AsyncOpenAI
from retriever import Retriever
from prompts import SYSTEM_PROMPT
from config import LLM_MODEL

logger = logging.getLogger(__name__)
client = AsyncOpenAI(api_key=os.environ["OPENAI_API_KEY"])
retriever = Retriever()

def build_context(chunks: list[dict]) -> str:
    parts = []
    parts.append("Support articles:")
    for chunk in chunks:
        parts.append(f"[{chunk['title']}]\n{chunk['text']}")
    return "\n\n---\n\n".join(parts)


def retrieve_chunks(query: str) -> list[dict]:
    return retriever.search(query)


async def stream_answer(query: str, history: list[dict]):
    logger.info("Generating response")
    chunks = retrieve_chunks(query)
    logger.debug(f"Retrieved {len(chunks)} chunks from vector store")
    context = build_context(chunks) if chunks else ""
    system = SYSTEM_PROMPT.format(context=context if context else "")

    messages = [{"role": "system", "content": system}, *history, {"role": "user", "content": query}]

    stream = await client.chat.completions.create(model=LLM_MODEL, messages=messages, stream=True)
    async for chunk in stream:
        delta = chunk.choices[0].delta.content
        if delta:
            yield delta
