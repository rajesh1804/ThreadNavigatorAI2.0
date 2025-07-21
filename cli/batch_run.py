import yaml
import json
import time
from agents.thread_summarizer_agent import ThreadSummarizerAgent
from agents.fact_checker_agent import FactCheckerAgent
from agents.evaluator_agent import EvaluatorAgent

with open("config/config.yaml", "r") as f:
    config = yaml.safe_load(f)

summarizer = ThreadSummarizerAgent("Summarizer", config)
fact_checker = FactCheckerAgent("FactChecker", config)
evaluator = EvaluatorAgent("Evaluator", config)

with open("data/threads_100.json", "r") as f:
    threads = json.load(f)

results = []
start_time = time.time()

for i, thread in enumerate(threads):
    thread_id = thread["thread_id"]
    title = thread["title"]
    thread_text = "\n".join(thread["posts"])
    latency = {}
    is_mock = i >= 1
    source_url = f"https://reddit.com/{thread_id}"

    # ✅ Model info extraction from config
    def get_model(agent_key):
        return config["agents"][agent_key.lower()]["model"]  #config.get(agent_key, {}).get("model", config.get("llm", {}).get("model", "unknown"))

    models_used = {
        "summarizer": get_model("summarizer"),
        "factchecker": get_model("factchecker"),
        "evaluator": get_model("evaluator"),
    }

    if not is_mock:
        print(f"[{i+1}/100] 🔁 Real run for {thread_id} ...")
        start = time.time()
        summary = summarizer.run(thread)
        latency["summarizer"] = round(time.time() - start, 2)

        start = time.time()
        facts = fact_checker.run(summary)
        latency["factchecker"] = round(time.time() - start, 2)

        start = time.time()
        eval_scores = evaluator.run(summary, thread_text)
        latency["evaluator"] = round(time.time() - start, 2)
    else:
        print(f"[{i+1}/100] 🤖 Simulated run for {thread_id} ...")

        summary = "\n".join([post.split(":", 1)[1].strip() for post in thread["posts"][:5]])
        facts = [{"claim": line, "judgment": "✅ Likely Correct"} for line in summary.split("\n") if line]
        eval_scores = {
            "relevance": {"score": 4, "reason": "Mocked: Covers most key ideas."},
            "factuality": {"score": 5, "reason": "Mocked: No contradiction found."},
            "coherence": {"score": 4, "reason": "Mocked: Bullet points well structured."}
        }
        latency = {"summarizer": 0.01, "factchecker": 0.01, "evaluator": 0.01}

    results.append({
        "thread_id": thread_id,
        "title": title,
        "posts": thread["posts"],
        "summary": summary,
        "fact_check": facts,
        "evaluation": eval_scores,
        "latency": latency,
        "models_used": models_used,
        "is_mock": is_mock,
        "source_url": source_url
    })

total_time = round(time.time() - start_time, 2)
print(f"\n✅ Completed all 100 threads in {total_time} seconds.")

with open("data/batch_output.json", "w") as f:
    json.dump(results, f, indent=2)

print("📦 Output saved to data/batch_output.json")
