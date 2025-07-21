class BaseAgent:
    def __init__(self, name, config):
        self.name = name
        self.config = config
        self.latency = None

    def run(self, input_text):
        raise NotImplementedError("Each agent must implement a run method.")
