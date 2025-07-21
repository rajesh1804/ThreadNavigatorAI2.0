from agents.base_agent import BaseAgent
import os
import httpx
from dotenv import load_dotenv

load_dotenv()

class SearchAgent(BaseAgent):
    def run(self, input_text):
        serper_api_key = os.getenv("SERPER_API_KEY")
        headers = {
            "X-API-KEY": serper_api_key,
            "Content-Type": "application/json"
        }

        query = input_text.strip()
        payload = {
            "q": query,
            "num": 3  # optional: limit number of results
        }

        try:
            response = httpx.post("https://google.serper.dev/search", json=payload, headers=headers, timeout=10.0)
            data = response.json()
            if "organic" in data and len(data["organic"]) > 0:
                bullets = []
                for item in data["organic"][:3]:
                    title = item.get("title", "")
                    snippet = item.get("snippet", "")
                    link = item.get("link", "")
                    bullets.append(f"- 🔗 [{title}]({link}): {snippet}")
                return "[Search Results from Google via Serper.dev]\n" + "\n".join(bullets)
            else:
                return "[Search Result] No relevant search results found."
        except Exception as e:
            return f"[Search Error] {str(e)}"
