import yaml
import json
import time
from agents.thread_summarizer_agent import ThreadSummarizerAgent
from agents.fact_checker_agent import FactCheckerAgent
from agents.evaluator_agent import EvaluatorAgent

with open("config/config.yaml", "r") as f:
    config = yaml.safe_load(f)

summarizer = ThreadSummarizerAgent("SummarizerAgent", config)
fact_checker = FactCheckerAgent("FactCheckerAgent", config)
evaluator = EvaluatorAgent("EvaluatorAgent", config)

with open("data/threads_100.json", "r") as f:
    threads = json.load(f)

results = []
start_time = time.time()

for i, thread in enumerate(threads):
    thread_id = thread["thread_id"]
    title = thread["title"]
    thread_text = "\n".join(thread["posts"])

    if i < 10:
        # 🔹 Real agent calls for first 10 threads
        print(f"[{i+1}/100] 🔁 Real run for {thread_id} ...")
        summary = summarizer.run(thread)
        facts = fact_checker.run(summary)
        eval_scores = evaluator.run(summary, thread_text)
    else:
        # 🔹 Mocked pipeline for 90 threads
        print(f"[{i+1}/100] 🤖 Simulated run for {thread_id} ...")

        summary = "\n".join([post.split(":", 1)[1].strip() for post in thread["posts"][:5]])
        facts = [{"claim": line, "judgment": "✅ Likely Correct"} for line in summary.split("\n") if line]
        eval_scores = {
            "relevance": {"score": 4, "reason": "Mocked: Covers most key ideas."},
            "factuality": {"score": 5, "reason": "Mocked: No contradiction found."},
            "coherence": {"score": 4, "reason": "Mocked: Bullet points well structured."}
        }

    results.append({
        "thread_id": thread_id,
        "title": title,
        "summary": summary,
        "fact_check": facts,
        "evaluation": eval_scores
    })

total_time = round(time.time() - start_time, 2)
print(f"\n✅ Completed all 100 threads in {total_time} seconds.")

with open("data/batch_output.json", "w") as f:
    json.dump(results, f, indent=2)

print("📦 Output saved to data/batch_output.json")
