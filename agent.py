import json
import logging
import os
from dataclasses import dataclass
from typing import AsyncGenerator

from openai import APIError, AsyncOpenAI, AuthenticationError, RateLimitError

from config import LLM_MODEL
from prompts import SYSTEM_PROMPT
from retriever import Retriever

logger = logging.getLogger(__name__)
client = AsyncOpenAI(api_key=os.environ["OPENAI_API_KEY"])
retriever = Retriever()

TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "search_knowledge_base",
            "description": (
                "Search Bynder's support knowledge base for articles relevant to a query. "
                "Use this tool whenever the user asks about Bynder features, how-tos, "
                "troubleshooting, integrations, permissions, or any product-related question. "
                "You can call this tool multiple times with different queries to gather "
                "more information if the first search didn't return enough context."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "A concise search query to find relevant support articles.",
                    }
                },
                "required": ["query"],
            },
        },
    }
]


@dataclass
class ToolCallEvent:
    name: str
    arguments: dict
    result: str


@dataclass
class TokenEvent:
    token: str


def build_context(chunks: list[dict]) -> str:
    parts = ["Support articles:"]
    for chunk in chunks:
        parts.append(f"[{chunk['title']}]\nSource: {chunk['source_url']}\n{chunk['text']}")
    return "\n\n---\n\n".join(parts)


def _format_chunks_summary(chunks: list[dict]) -> str:
    if not chunks:
        return "No relevant articles found."
    return "\n\n".join(
        f"[{c['title']}] (score: {c['score']})\n{c['source_url']}" for c in chunks
    )


def _execute_tool(name: str, args: dict) -> tuple[str, list[dict]]:
    if name == "search_knowledge_base":
        try:
            chunks = retriever.search(args["query"])
        except Exception as e:
            logger.error(f"Knowledge base search error: {e}")
            return "Error: Unable to search the knowledge base at this time.", []
        tool_result = build_context(chunks) if chunks else "No relevant articles found."
        return tool_result, chunks
    return f"Unknown tool: {name}", []


async def run_agent(
    query: str,
    history: list[dict],
) -> AsyncGenerator[ToolCallEvent | TokenEvent, None]:
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        *history,
        {"role": "user", "content": query},
    ]

    while True:
        try:
            stream = await client.chat.completions.create(
                model=LLM_MODEL,
                messages=messages,
                tools=TOOLS,
                stream=True,
            )
        except AuthenticationError:
            yield TokenEvent("Authentication error with the AI service. Please check the API key.")
            return
        except RateLimitError:
            yield TokenEvent("Rate limit reached. Please try again in a moment.")
            return
        except APIError as e:
            logger.error(f"OpenAI API error: {e}")
            yield TokenEvent("I encountered an error while processing your request. Please try again.")
            return

        tool_calls_acc: dict[int, dict] = {}

        async for chunk in stream:
            delta = chunk.choices[0].delta

            if delta.tool_calls:
                for tc_delta in delta.tool_calls:
                    idx = tc_delta.index
                    if idx not in tool_calls_acc:
                        tool_calls_acc[idx] = {"id": "", "name": "", "arguments": ""}
                    if tc_delta.id:
                        tool_calls_acc[idx]["id"] = tc_delta.id
                    if tc_delta.function and tc_delta.function.name:
                        tool_calls_acc[idx]["name"] = tc_delta.function.name
                    if tc_delta.function and tc_delta.function.arguments:
                        tool_calls_acc[idx]["arguments"] += tc_delta.function.arguments

            if delta.content:
                yield TokenEvent(delta.content)

        if not tool_calls_acc:
            break

        assistant_msg = {
            "role": "assistant",
            "tool_calls": [
                {
                    "id": tc["id"],
                    "type": "function",
                    "function": {"name": tc["name"], "arguments": tc["arguments"]},
                }
                for tc in tool_calls_acc.values()
            ],
        }
        messages.append(assistant_msg)

        for tc in tool_calls_acc.values():
            args = json.loads(tc["arguments"])
            tool_result, chunks = _execute_tool(tc["name"], args)

            yield ToolCallEvent(
                name=tc["name"],
                arguments=args,
                result=_format_chunks_summary(chunks),
            )

            messages.append({
                "role": "tool",
                "tool_call_id": tc["id"],
                "content": tool_result,
            })
