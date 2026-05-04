from utils.gemini_client import generate

def translate(text: str, target_lang: str, style: str) -> str:
    style_map = {
        "自然な表現": "自然で流暢な表現を優先し、",
        "直訳寄り": "原文に忠実な直訳を心がけ、",
        "ビジネス向け": "ビジネスシーンに適した丁寧な表現で、",
        "カジュアル": "カジュアルで親しみやすい表現で、",
    }
    prompt = f"""以下の文章を{target_lang}に翻訳してください。

{style_map.get(style, '')}翻訳してください。

翻訳後の文章のみを出力してください（説明不要）。

【翻訳対象】
{text}"""
    return generate(prompt)
