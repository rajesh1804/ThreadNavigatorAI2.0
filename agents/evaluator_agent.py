from agents.base_agent import BaseAgent
from utils.llm_client import chat_completion
import json

class EvaluatorAgent(BaseAgent):
    def run(self, summary_text, thread_text):
        messages = [
            {"role": "system", "content": "You are an expert evaluator for Reddit thread summaries. Your task is to score summaries on three metrics:\n\n1. Relevance (does it capture the main ideas of the thread?)\n2. Factuality (does it reflect what was actually said in the thread?)\n3. Coherence (is it well-structured, readable, and logically organized?)\n\nGive each metric a score from 1 to 5 and explain your reasoning briefly."},
            {"role": "user", "content": f"Thread:\n{thread_text}\n\nSummary:\n{summary_text}\n\nPlease evaluate this summary based on the three metrics and respond in JSON format like:\n{{\n  \"relevance\": {{\"score\": x, \"reason\": \"...\"}},\n  \"factuality\": {{\"score\": x, \"reason\": \"...\"}},\n  \"coherence\": {{\"score\": x, \"reason\": \"...\"}}\n}}"}
        ]

        llm_config = self.config["llm"]
        response = chat_completion(
            messages=messages,
            model=llm_config.get("model", "mistralai/mistral-7b-instruct:free"),
            temperature=llm_config.get("temperature", 0.7),
            max_tokens=1024
        )

        try:
            parsed = json.loads(response)
        except json.JSONDecodeError:
            parsed = {"relevance": {"score": 0, "reason": "Invalid JSON from LLM"},
                    "factuality": {"score": 0, "reason": "Invalid JSON from LLM"},
                    "coherence": {"score": 0, "reason": "Invalid JSON from LLM"}}

        return parsed
