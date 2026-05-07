import os
from openai import AsyncOpenAI
from retriever import Retriever
from prompts import SYSTEM_PROMPT
from config import LLM_MODEL

client = AsyncOpenAI(api_key=os.environ["OPENAI_API_KEY"])
retriever = Retriever()

def build_context(chunks: list[dict]) -> str:
    parts = []
    for chunk in chunks:
        parts.append(f"[{chunk['title']}]\n{chunk['text']}")
    return "\n\n---\n\n".join(parts)

async def stream_answer(query: str, history: list[dict]):
    chunks = retriever.search(query)
    context = build_context(chunks)
    system = SYSTEM_PROMPT.format(context=context)

    messages = [{"role": "system", "content": system}, *history, {"role": "user", "content": query}]

    stream = await client.chat.completions.create(model=LLM_MODEL, messages=messages, stream=True)
    async for chunk in stream:
        delta = chunk.choices[0].delta.content
        if delta:
            yield delta