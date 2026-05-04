from utils.gemini_client import generate

def brainstorm(theme: str, count: int, perspective: str) -> str:
    prompt = f"""「{theme}」について、{perspective}の観点からアイデアを{count}個ブレインストーミングしてください。

各アイデアは番号付きリストで出力し、それぞれに2〜3行の説明を加えてください。
斬新なアイデアと現実的なアイデアをバランスよく混ぜてください。"""
    return generate(prompt)
