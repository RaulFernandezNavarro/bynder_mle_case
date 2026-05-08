import logging

import chainlit as cl
from dotenv import load_dotenv

from logging_config import setup_logging

load_dotenv()
setup_logging()

from agent import retrieve, rewrite_query, stream_answer

logger = logging.getLogger(__name__)


@cl.on_chat_start
async def start():
    cl.user_session.set("history", [])
    logger.info("Chat session started")


@cl.on_message
async def on_message(message: cl.Message):
    logger.info("Received user message")
    history = cl.user_session.get("history")

    async with cl.Step(name="Query rewrite", type="llm") as step:
        search_query = await rewrite_query(message.content, history)
        step.input = message.content
        step.output = search_query

    async with cl.Step(name="Retrieval") as step:
        chunks = retrieve(search_query)
        step.input = search_query
        step.output = (
            "\n\n".join(
                f"[{c['title']}] (score: {c['score']})\n{c['source_url']}"
                for c in chunks
            )
            or "No chunks retrieved."
        )

    response = cl.Message(content="")
    await response.send()

    full_response = ""
    async for token in stream_answer(message.content, chunks, history):
        await response.stream_token(token)
        full_response += token

    await response.update()

    history.append({"role": "user", "content": message.content})
    history.append({"role": "assistant", "content": full_response})
    cl.user_session.set("history", history)
