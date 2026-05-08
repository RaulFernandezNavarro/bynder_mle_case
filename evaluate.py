import argparse
import asyncio
import logging

from dotenv import load_dotenv

from logging_config import setup_logging

load_dotenv()
setup_logging(level="WARNING")

from agent import TokenEvent, ToolCallEvent, run_agent

logger = logging.getLogger(__name__)

TEST_QUESTIONS = [
    {
        "id": 1,
        "category": "Simple lookup",
        "messages": [
            "What keyboard shortcut can I use to download an asset in the Asset Bank?"
        ],
        "expected_keywords": ["keyboard", "shortcut"],
    },
    {
        "id": 2,
        "category": "Simple lookup",
        "messages": [
            "What file format do I need for uploading 360-degree images to Bynder?"
        ],
        "expected_keywords": ["360", "format"],
    },
    {
        "id": 3,
        "category": "How-to",
        "messages": [
            "How do I enable automatic transcription for my video files so the spoken content becomes searchable?"
        ],
        "expected_keywords": ["transcription", "video"],
    },
    {
        "id": 4,
        "category": "How-to",
        "messages": ["How do I set up an OAuth2 integration with Bynder's API?"],
        "expected_keywords": ["oauth", "app"],
    },
    {
        "id": 5,
        "category": "Feature comparison",
        "messages": [
            "What's the difference between DAT Presets and creating a DAT derivative on-the-fly?"
        ],
        "expected_keywords": ["preset", "derivative"],
    },
    {
        "id": 6,
        "category": "Multi-article synthesis",
        "messages": [
            "I want to find duplicate assets before uploading and also manage existing duplicates already in my Asset Bank. What options does Bynder offer?"
        ],
        "expected_keywords": ["duplicate"],
    },
    {
        "id": 7,
        "category": "Permissions",
        "messages": [
            "What are the different permission levels for Collections, and what can each level do?"
        ],
        "expected_keywords": ["permission", "collection"],
    },
    {
        "id": 8,
        "category": "Security / compliance",
        "messages": [
            "What security certifications does Bynder hold and where is my data stored?"
        ],
        "expected_keywords": ["security", "certif"],
    },
    {
        "id": 9,
        "category": "Follow-up (conversational memory)",
        "messages": [
            "How do I create a metadata preset?",
            "Can I share that preset with specific users only?",
        ],
        "expected_keywords": ["preset", "share"],
    },
]


async def run_question(question: dict) -> dict:
    history = []
    turns = []

    for user_msg in question["messages"]:
        tool_calls = []
        answer_tokens = []

        async for event in run_agent(user_msg, history):
            if isinstance(event, ToolCallEvent):
                tool_calls.append(
                    {
                        "query": event.arguments.get("query", ""),
                        "results_summary": event.result,
                    }
                )
            elif isinstance(event, TokenEvent):
                answer_tokens.append(event.token)

        answer = "".join(answer_tokens)
        history.append({"role": "user", "content": user_msg})
        history.append({"role": "assistant", "content": answer})

        turns.append(
            {
                "user": user_msg,
                "tool_calls": tool_calls,
                "answer": answer,
            }
        )

    final_answer = turns[-1]["answer"].lower()
    keywords_found = [
        kw for kw in question.get("expected_keywords", []) if kw in final_answer
    ]
    keywords_missing = [
        kw for kw in question.get("expected_keywords", []) if kw not in final_answer
    ]

    return {
        "id": question["id"],
        "category": question["category"],
        "turns": turns,
        "keywords_found": keywords_found,
        "keywords_missing": keywords_missing,
    }


async def main():
    parser = argparse.ArgumentParser(description="Evaluate the Bynder support agent")
    parser.add_argument("--question", type=int, help="Run only this question number")
    args = parser.parse_args()

    questions = TEST_QUESTIONS
    if args.question:
        questions = [q for q in TEST_QUESTIONS if q["id"] == args.question]

    results = []
    for q in questions:
        print(f"\n{'=' * 60}")
        print(f"Question {q['id']}: {q['category']}")
        print(f"{'=' * 60}")

        result = await run_question(q)
        results.append(result)

        for turn in result["turns"]:
            print(f"\nUser: {turn['user']}")
            for tc in turn["tool_calls"]:
                print(f"  [Tool] search: {tc['query']}")
            print(f"\nAssistant: {turn['answer'][:500]}")
            if len(turn["answer"]) > 500:
                print("...")

        if result["keywords_missing"]:
            print(f"\n  WARN: Missing expected keywords: {result['keywords_missing']}")
        else:
            print(f"\n  OK: All expected keywords found")

    print(f"\n\n{'=' * 60}")
    print("SUMMARY")
    print(f"{'=' * 60}")
    passed = sum(1 for r in results if not r["keywords_missing"])
    print(f"Passed: {passed}/{len(results)}")
    for r in results:
        status = (
            "PASS"
            if not r["keywords_missing"]
            else f"WARN (missing: {r['keywords_missing']})"
        )
        print(f"  Q{r['id']} [{r['category']}]: {status}")


if __name__ == "__main__":
    asyncio.run(main())
