from utils.gemini_client import generate

def generate_sns_post(content: str, platform: str, tone: str, hashtag: bool) -> str:
    platform_map = {
        "Twitter/X": "Twitter/X（140文字以内）",
        "Instagram": "Instagram（キャプション、改行を活用）",
        "Facebook": "Facebook（少し長めでも可）",
        "LinkedIn": "LinkedIn（プロフェッショナルな内容）",
        "Threads": "Threads（500文字以内）",
    }
    hashtag_instruction = "末尾に関連するハッシュタグを5〜8個追加してください。" if hashtag else "ハッシュタグは不要です。"

    prompt = f"""以下の内容をもとに{platform_map.get(platform, platform)}用の投稿文を日本語で作成してください。

文体・トーン: {tone}
{hashtag_instruction}

【投稿したい内容・テーマ】
{content}

投稿文を3パターン提案してください。各パターンに番号を付けてください。"""
    return generate(prompt)
