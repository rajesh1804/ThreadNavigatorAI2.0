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

        # llm_config = self.config.get("llm", {})
        # response = chat_completion(
        #     messages=messages,
        #     model=llm_config.get("model", "mistralai/mistral-7b-instruct:free"),
        #     temperature=llm_config.get("temperature", 0.7),
        #     max_tokens=llm_config.get("max_tokens", 1024)
        # )

        agent_config = self.config.get("agents", {}).get(self.name.lower(), {})
        llm_config = {
            "model": agent_config.get("model", self.config["llm"]["model"]),
            "temperature": agent_config.get("temperature", self.config["llm"]["temperature"]),
            "max_tokens": agent_config.get("max_tokens", self.config["llm"]["max_tokens"])
        }

        print(f"Summarizer Using model: {llm_config['model']} with temperature {llm_config['temperature']} and max tokens {llm_config['max_tokens']}")

        return chat_completion(
            messages=messages,
            model=llm_config["model"],
            temperature=llm_config["temperature"],
            max_tokens=llm_config["max_tokens"]
        )

        return response
