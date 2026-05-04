import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

DEFAULT_MODEL = "gemini-3-flash-preview"

def _get_client() -> genai.Client:
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key or api_key == "your_api_key_here":
        raise ValueError("GEMINI_API_KEY が設定されていません。.env ファイルを確認してください。")
    return genai.Client(api_key=api_key)

def generate(prompt: str, model_name: str = DEFAULT_MODEL) -> str:
    client = _get_client()
    response = client.models.generate_content(model=model_name, contents=prompt)
    return response.text
