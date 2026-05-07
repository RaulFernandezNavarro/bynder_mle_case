import os
from dotenv import load_dotenv
import asyncio
load_dotenv()

from agent import stream_answer

QUESTIONS = [
    "What keyboard shortcut can I use to download an asset in the Asset Bank?",
    "What file format do I need for uploading 360-degree images to Bynder?",
    "How do I enable automatic transcription for my video files so the spoken content becomes searchable?",
    "How do I set up an OAuth2 integration with Bynder's API?",
    "What's the difference between DAT Presets and creating a DAT derivative on-the-fly?",
    "I want to find duplicate assets before uploading and also manage existing duplicates already in my Asset Bank. What options does Bynder offer?",
    "What are the different permission levels for Collections, and what can each level do?",
    "What security certifications does Bynder hold and where is my data stored?",
]

FOLLOWUP = [
    "How do I create a metadata preset?",
    "Can I share that preset with specific users only?",
]

async def run():
    for i, question in enumerate(QUESTIONS, 1):
        print(f"\n{'='*60}\nQ{i}: {question}\n{'='*60}")
        answer = "".join(stream_answer(question, []))
        print(answer)

    print(f"\n{'='*60}\nFollow-up conversation\n{'='*60}")
    history = []
    for question in FOLLOWUP:
        print(f"\nUser: {question}")
        answer = "".join(stream_answer(question, history))
        print(f"Agent: {answer}")
        history.append({"role": "user", "content": question})
        history.append({"role": "assistant", "content": answer})

if __name__ == "__main__":
     asyncio.run(run())