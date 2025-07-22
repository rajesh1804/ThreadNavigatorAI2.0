from agents.base_agent import BaseAgent
from utils.llm_client import chat_completion
import json
from pprint import pprint

class EvaluatorAgent(BaseAgent):
    def run(self, summary_text, thread_text):
        messages = [
            {"role": "system", "content": "You are an expert evaluator for Reddit thread summaries. Your task is to score summaries on three metrics:\n\n1. Relevance (does it capture the main ideas of the thread?)\n2. Factuality (does it reflect what was actually said in the thread?)\n3. Coherence (is it well-structured, readable, and logically organized?)\n\nGive each metric a score from 1 to 5 and explain your reasoning briefly."},
            {"role": "user", "content": f"Thread:\n{thread_text}\n\nSummary:\n{summary_text}\n\nPlease evaluate this summary based on the three metrics and respond in JSON format like:\n{{\n  \"relevance\": {{\"score\": x, \"reason\": \"...\"}},\n  \"factuality\": {{\"score\": x, \"reason\": \"...\"}},\n  \"coherence\": {{\"score\": x, \"reason\": \"...\"}}\n}}"}
        ]

        # llm_config = self.config["llm"]
        # response = chat_completion(
        #     messages=messages,
        #     model=llm_config.get("model", "mistralai/mistral-7b-instruct:free"),
        #     temperature=llm_config.get("temperature", 0.7),
        #     max_tokens=1024
        # )

        agent_config = self.config.get("agents", {}).get(self.name.lower(), {})
        llm_config = {
            "model": agent_config.get("model", self.config["llm"]["model"]),
            "temperature": agent_config.get("temperature", self.config["llm"]["temperature"]),
            "max_tokens": agent_config.get("max_tokens", self.config["llm"]["max_tokens"])
        }
        print(f"Evaluator Using model: {llm_config['model']} with temperature {llm_config['temperature']} and max tokens {llm_config['max_tokens']}")
        print(f"Evaluator messages: {messages}")
        print(f"Evaluator llm_config config: {llm_config}")
        response = chat_completion(
            messages=messages,
            model=llm_config["model"],
            temperature=llm_config["temperature"],
            max_tokens=llm_config["max_tokens"]
        )

        # pprint(f"Error parsing JSON response: {response}")

        try:
            parsed = json.loads(response)
        except json.JSONDecodeError:
            pprint(f"Error parsing JSON response: {response}")
            parsed = {"relevance": {"score": 0, "reason": "Invalid JSON from LLM"},
                    "factuality": {"score": 0, "reason": "Invalid JSON from LLM"},
                    "coherence": {"score": 0, "reason": "Invalid JSON from LLM"}}

        return parsed
