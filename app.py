import chainlit as cl
from dotenv import load_dotenv
load_dotenv()

from agent import stream_answer

@cl.on_chat_start
async def start():
    cl.user_session.set("history", [])

@cl.on_message
async def on_message(message: cl.Message):
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