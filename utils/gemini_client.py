import contextvars
import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

DEFAULT_MODEL = "gemini-3-flash-preview"

# セッションごとのAPIキーを保持（スレッドセーフ）
_session_api_key: contextvars.ContextVar[str] = contextvars.ContextVar("session_api_key", default="")

def set_session_api_key(key: str) -> None:
    """現在のスレッド（Streamlitセッション）のAPIキーをセットする。"""
    _session_api_key.set(key)

def _get_client() -> genai.Client:
    api_key = _session_api_key.get() or os.getenv("GEMINI_API_KEY", "")
    if not api_key or api_key == "your_api_key_here":
        raise ValueError("GEMINI_API_KEY が設定されていません。.env ファイルを確認してください。")
    return genai.Client(api_key=api_key)

def generate(prompt: str, model_name: str = DEFAULT_MODEL) -> str:
    client = _get_client()
    response = client.models.generate_content(model=model_name, contents=prompt)
    return response.text
