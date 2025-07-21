from agents.base_agent import BaseAgent
from utils.llm_client import chat_completion

class ThreadSummarizerAgent(BaseAgent):
    def run(self, thread):
        title = thread.get("title", "")
        posts = thread.get("posts", [])
        thread_text = "\n".join(posts)

        messages = [
            {"role": "system", "content": "You are a helpful assistant that summarizes Reddit threads into concise bullet points."},
            {"role": "user", "content": f"Title: {title}\n\nThread:\n{thread_text}\n\nSummarize the key takeaways in 4-6 bullet points."}
        ]

        llm_config = self.config.get("llm", {})
        response = chat_completion(
            messages=messages,
            model=llm_config.get("model", "mistralai/mistral-7b-instruct:free"),
            temperature=llm_config.get("temperature", 0.7),
            max_tokens=llm_config.get("max_tokens", 1024)
        )

        return response
