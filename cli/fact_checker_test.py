import yaml
from agents.fact_checker_agent import FactCheckerAgent
import json

with open("config/config.yaml", "r") as f:
    config = yaml.safe_load(f)

agent = FactCheckerAgent("FactCheckerAgent", config)

summary_input = """
- iPhones generally have better battery life than most Android phones.
- LangChain is preferred over Haystack for production RAG pipelines.
- Weekly standups improve productivity in remote ML teams.
- Android 14 supports iMessage natively.
"""

print("\n🔎 Fact Checking Summary:\n")
results = agent.run(summary_input)

print(json.dumps(results, indent=2))
