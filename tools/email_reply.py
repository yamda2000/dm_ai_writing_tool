from utils.gemini_client import generate

def reply_email(original: str, intent: str, tone: str, your_name: str) -> str:
    prompt = f"""以下のメールに対する返信文を日本語で作成してください。

【受信メール】
{original}

【返信の意図・要点】
{intent}

【文体】: {tone}
【差出人名】: {your_name if your_name else '（名前なし）'}

返信メールとして適切なフォーマット（宛名・本文・締め・署名）で出力してください。"""
    return generate(prompt)
