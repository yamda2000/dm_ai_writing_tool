from utils.gemini_client import generate

def generate_catchphrases(product: str, features: str, target: str, count: int) -> str:
    prompt = f"""以下の商品・サービスのキャッチコピーを{count}個、日本語で提案してください。

商品・サービス名: {product}
特徴・強み: {features}
ターゲット: {target if target else '一般消費者'}

各キャッチコピーは番号付きリストで出力し、それぞれの訴求ポイント（何を伝えようとしているか）を一言で添えてください。
短いもの（10文字以内）と中程度（20〜30文字）を混ぜて提案してください。"""
    return generate(prompt)
