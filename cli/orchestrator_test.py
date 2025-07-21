import yaml
from agents._deprecated.orchestrator_agent import OrchestratorAgent
import json

with open("config/config.yaml", "r") as f:
    config = yaml.safe_load(f)

agent = OrchestratorAgent("Orchestrator", config)
query = "What is LangChain and how is it used in AI?"

output = agent.run(query)

print("\n🧵 Final Output:\n")
print(json.dumps(output, indent=2))
