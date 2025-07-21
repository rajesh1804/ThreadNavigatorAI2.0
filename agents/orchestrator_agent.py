import time
from agents.base_agent import BaseAgent
from agents.search_agent import SearchAgent
from agents.summarizer_agent import SummarizerAgent

class OrchestratorAgent(BaseAgent):
    def __init__(self, name, config):
        super().__init__(name, config)
        self.search_agent = SearchAgent("SearchAgent", config)
        self.summarizer_agent = SummarizerAgent("SummarizerAgent", config)

    def run(self, query):
        timings = {}
        result = {}

        # Step 1: Search
        start = time.time()
        search_result = self.search_agent.run(query)
        timings["search"] = round(time.time() - start, 2)
        result["search_output"] = search_result

        # Step 2: Summarize
        start = time.time()
        summary = self.summarizer_agent.run(search_result)
        timings["summarize"] = round(time.time() - start, 2)
        result["summary"] = summary

        return {
            "input_query": query,
            "agent_outputs": result,
            "latency_seconds": timings
        }
