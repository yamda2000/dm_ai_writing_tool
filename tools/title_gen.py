from utils.gemini_client import generate

def generate_titles(content: str, count: int, style: str) -> str:
    prompt = f"""以下の記事内容に合う魅力的なタイトルを{count}個、日本語で提案してください。

スタイル: {style}

各タイトルは番号付きリストで出力し、それぞれに一言コメント（なぜ良いか）を添えてください。

【記事内容・テーマ】
{content}"""
    return generate(prompt)
