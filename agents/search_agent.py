from agents.base_agent import BaseAgent
import httpx

class SearchAgent(BaseAgent):
    def run(self, input_text):
        query = input_text.strip()
        url = f"https://api.duckduckgo.com/?q={query}&format=json&no_html=1"

        try:
            response = httpx.get(url, timeout=5.0)
            data = response.json()
            abstract = data.get("AbstractText")
            if abstract:
                return f"[Search Result] {abstract}"
            else:
                return "[Search Result] No direct answer found. Try refining your query."
        except Exception as e:
            return f"[Search Error] {str(e)}"
