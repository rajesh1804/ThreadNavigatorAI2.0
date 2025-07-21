import os
import openai
from dotenv import load_dotenv
from tenacity import retry, stop_after_attempt, wait_random_exponential, retry_if_exception_type

# Load .env variables
load_dotenv()

# Setup OpenRouter
openai.api_key = os.getenv("OPENROUTER_API_KEY")
openai.api_base = "https://openrouter.ai/api/v1"

@retry(
    stop=stop_after_attempt(3),
    wait=wait_random_exponential(min=1, max=4),
    retry=retry_if_exception_type(Exception)
)
def chat_completion(messages, model="mistralai/mistral-7b-instruct:free", temperature=0.7, max_tokens=1024):
    try:
        response = openai.ChatCompletion.create(
            model=model,
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"[LLM Error] {str(e)}"
