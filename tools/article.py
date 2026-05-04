from utils.gemini_client import generate

def write_article(theme: str, length: str, tone: str, target: str, keywords: str) -> str:
    length_map = {"短め（500字程度）": "約500文字", "普通（1000字程度）": "約1000文字", "長め（2000字程度）": "約2000文字"}
    prompt = f"""以下の条件で日本語の記事を執筆してください。

テーマ: {theme}
文字数: {length_map.get(length, '約1000文字')}
文体・トーン: {tone}
ターゲット読者: {target if target else '一般読者'}
含めるキーワード: {keywords if keywords else 'なし'}

構成は「導入→本文（2〜3セクション）→まとめ」の形式にしてください。
見出しは ## で記述してください。"""
    return generate(prompt)
