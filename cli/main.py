import yaml
from agents.search_agent import SearchAgent

with open("config/config.yaml", "r") as f:
    config = yaml.safe_load(f)

# agent = SearchAgent("SearchAgent", config)
# result = agent.run("What is the capital of France?")
# print(result)

query = "Python programming language"
agent = SearchAgent("SearchAgent", config)
result = agent.run(query)
print(f"Query: {query}")
print(result)