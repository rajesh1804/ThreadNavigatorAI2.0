from agents.base_agent import BaseAgent
from utils.llm_client import chat_completion

class SummarizerAgent(BaseAgent):
    def run(self, input_text):
        messages = [
            {"role": "system", "content": "You are a helpful assistant that summarizes Reddit threads or search results."},
            {"role": "user", "content": f"Summarize the following in 3–5 bullet points:\n\n{input_text}"}
        ]

        llm_config = self.config.get("llm", {})
        response = chat_completion(
            messages=messages,
            model=llm_config.get("model", "mistralai/mistral-7b-instruct:free"),
            temperature=llm_config.get("temperature", 0.7),
            max_tokens=llm_config.get("max_tokens", 1024)
        )

        return response
