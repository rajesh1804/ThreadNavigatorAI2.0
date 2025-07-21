import json
import random

topics = [
    "Best AI tools in 2025", "Switching from iPhone to Android", "Remote ML engineering tips",
    "LangChain vs LlamaIndex", "Python vs Rust for LLMs", "Favorite coding music",
    "Prompt engineering strategies", "Scaling RAG pipelines", "Fine-tuning vs adapters"
]

users = ["OP", "User1", "User2", "User3", "User4", "User5"]
comments = [
    "I personally prefer {X} because it's more flexible.",
    "Anyone tried using {X} with open source LLMs?",
    "{X} was great for us, especially with async support.",
    "Honestly, I think {X} is overhyped.",
    "We saw a 2x latency improvement using {X}.",
    "Not sure how {X} compares to {Y}, thoughts?",
    "Interesting take — I use {X} in prod daily.",
    "We switched from {Y} to {X} and never looked back."
]

def generate_thread(i):
    topic = random.choice(topics)
    keyword_x = topic.split()[0]
    keyword_y = random.choice([t.split()[0] for t in topics if t != topic])

    return {
        "thread_id": f"thread_{i:03}",
        "title": topic,
        "posts": [f"{user}: {random.choice(comments).format(X=keyword_x, Y=keyword_y)}" for user in users]
    }

threads = [generate_thread(i) for i in range(1, 101)]

with open("data/threads_100.json", "w") as f:
    json.dump(threads, f, indent=2)

print("✅ Generated 100 synthetic threads.")
