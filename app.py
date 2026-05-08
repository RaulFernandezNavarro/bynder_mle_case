import logging

import chainlit as cl
from dotenv import load_dotenv

from logging_config import setup_logging

load_dotenv()
setup_logging()

from agent import TokenEvent, ToolCallEvent, run_agent

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
    response_sent = False
    full_response = ""
    sources: dict[str, str] = {}

    try:
        async for event in run_agent(message.content, history):
            if isinstance(event, ToolCallEvent):
                async with cl.Step(name=f"Searching: {event.arguments.get('query', '')}", type="tool") as step:
                    step.input = event.arguments.get("query", "")
                    step.output = event.result
                for chunk in event.chunks:
                    if chunk["source_url"]:
                        sources[chunk["title"]] = chunk["source_url"]
            elif isinstance(event, TokenEvent):
                if not response_sent:
                    await response.send()
                    response_sent = True
                await response.stream_token(event.token)
                full_response += event.token
    except Exception as e:
        logger.error(f"Unexpected error: {e}", exc_info=True)
        full_response = "Something went wrong. Please try again or start a new chat."
        if not response_sent:
            await response.send()
        await response.stream_token(full_response)

    if sources:
        citations = "\n".join(f"- [{title}]({url})" for title, url in sources.items())
        source_section = f"\n\n**Sources:**\n{citations}"
        await response.stream_token(source_section)
        full_response += source_section

    await response.update()

    history.append({"role": "user", "content": message.content})
    history.append({"role": "assistant", "content": full_response})
    cl.user_session.set("history", history)
