from agents.base_agent import BaseAgent
import yaml

with open("config/config.yaml", "r") as f:
    config = yaml.safe_load(f)

class DummyAgent(BaseAgent):
    def run(self, input_text):
        return f"{self.name} received input: {input_text}"

agent = DummyAgent("TestAgent", config)
print(agent.run("This is a test input"))
