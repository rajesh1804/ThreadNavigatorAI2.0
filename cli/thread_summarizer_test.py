import yaml
import json
from agents.thread_summarizer_agent import ThreadSummarizerAgent

with open("config/config.yaml", "r") as f:
    config = yaml.safe_load(f)

with open("data/threads.json", "r") as f:
    threads = json.load(f)

agent = ThreadSummarizerAgent("ThreadSummarizer", config)

for thread in threads:
    print("\n🧵 Title:", thread["title"])
    summary = agent.run(thread)
    print("🔍 Summary:\n", summary)
    print("-" * 60)
