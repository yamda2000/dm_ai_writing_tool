from utils.gemini_client import generate

def summarize(text: str, style: str, length: str) -> str:
    length_map = {
        "1〜2文": "1〜2文（超短縮）",
        "3〜5文": "3〜5文",
        "箇条書き5点": "箇条書き5点以内",
        "200字程度": "200文字程度",
    }
    style_map = {
        "ニュートラル": "客観的・中立的なトーンで",
        "わかりやすく": "専門用語を避け、誰でも理解できる表現で",
        "ビジネス向け": "ビジネス文書として適切な表現で",
    }
    prompt = f"""以下の文章を日本語で要約してください。

{style_map.get(style, '')}
要約の長さ: {length_map.get(length, '3〜5文')}

【文章】
{text}"""
    return generate(prompt)
