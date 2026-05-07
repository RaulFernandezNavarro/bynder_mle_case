import logging
import chainlit as cl
from dotenv import load_dotenv

from logging_config import setup_logging

load_dotenv()
setup_logging()

from agent import stream_answer


logger = logging.getLogger(__name__)


@cl.on_chat_start
async def start():
    cl.user_session.set("history", [])
    logger.info("Chat session started")

@cl.on_message
async def on_message(message: cl.Message):
    logger.info("Received user message")
    history = cl.user_session.get("history")

    response = cl.Message(content="")
    await response.send()

    full_response = ""
    async for token in stream_answer(message.content, history):
        await response.stream_token(token)
        full_response += token

    await response.update()

    history.append({"role": "user", "content": message.content})
    history.append({"role": "assistant", "content": full_response})
    cl.user_session.set("history", history)
    logger.debug("Conversation history updated")
