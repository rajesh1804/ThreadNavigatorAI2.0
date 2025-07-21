from agents.base_agent import BaseAgent
from agents.search_agent import SearchAgent
from utils.llm_client import chat_completion

class FactCheckerAgent(BaseAgent):
    def __init__(self, name, config):
        super().__init__(name, config)
        self.search_agent = SearchAgent("SearchAgent", config)

    def run(self, summary_bullets):
        claims = summary_bullets.strip().split("\n")
        checked_claims = []

        for claim in claims:
            if not claim.strip():
                continue

            # Search the web for evidence
            search_result = self.search_agent.run(claim)

            # Let LLM decide: Is the claim supported or not?
            messages = [
                {"role": "system", "content": "You are a fact-checking assistant. Classify the following claim as one of:\n\n✅ Likely Correct\n❌ Likely Incorrect\n🤷 Unverifiable\n\nUse the search result provided as evidence."},
                {"role": "user", "content": f"Claim: {claim}\n\nEvidence:\n{search_result}\n\nClassify and explain your reasoning briefly."}
            ]

            # response = chat_completion(
            #     messages=messages,
            #     model=self.config["llm"]["model"],
            #     temperature=self.config["llm"]["temperature"],
            #     max_tokens=512
            # )

            agent_config = self.config.get("agents", {}).get(self.name.lower(), {})
            llm_config = {
                "model": agent_config.get("model", self.config["llm"]["model"]),
                "temperature": agent_config.get("temperature", self.config["llm"]["temperature"]),
                "max_tokens": agent_config.get("max_tokens", self.config["llm"]["max_tokens"])
            }

            response = chat_completion(
                messages=messages,
                model=llm_config["model"],
                temperature=llm_config["temperature"],
                max_tokens=llm_config["max_tokens"]
            )

            print(f"Fact Checker Using model: {llm_config['model']} with temperature {llm_config['temperature']} and max tokens {llm_config['max_tokens']}")


            checked_claims.append({
                "claim": claim,
                "judgment": response
            })

        return checked_claims
