# AI ライティングツール

Streamlit + Python + Google Gemini API で構築した個人用 AI ライティングツールです。
記事執筆・メール返信・翻訳など 9 種類のライティング機能を 1 つの画面から利用できます。

---

## 機能一覧

| 機能 | 概要 |
|------|------|
| 📝 記事執筆 | テーマ・文字数・トーン・キーワードを指定してブログ記事を生成 |
| 📧 メール返信 | 受信メールを貼り付けて返信文を自動作成 |
| 📋 文章要約 | 長文を指定したスタイル・長さで要約 |
| 🏷️ タイトル生成 | 記事内容から魅力的なタイトル候補を複数提案 |
| 🔍 文章校正 | 誤字脱字修正・表現改善・ビジネス文書化など 4 モード |
| 💡 キャッチコピー生成 | 商品・サービスのキャッチコピーを複数パターン提案 |
| 📱 SNS 投稿文生成 | Twitter/X・Instagram など各 SNS 向けに 3 パターン生成 |
| 🌐 翻訳 | 12 言語対応・翻訳スタイル選択可 |
| 🧠 ブレインストーミング | テーマと視点を指定してアイデアを発散 |

---

## 技術スタック

- **Python** 3.11
- **Streamlit** 1.57 — UI フレームワーク
- **Google Generative AI SDK** (`google-generativeai`) — Gemini API クライアント
- **python-dotenv** — 環境変数管理

---

## ファイル構成

```
20260504_claudecode_aiapp/
├── app.py                  # メインアプリ（Streamlit エントリポイント）
├── .env                    # APIキー設定（git 管理外推奨）
├── requirements.txt        # 依存パッケージ一覧
├── utils/
│   ├── __init__.py
│   └── gemini_client.py    # Gemini API 共通クライアント
└── tools/
    ├── __init__.py
    ├── article.py          # 記事執筆
    ├── email_reply.py      # メール返信
    ├── summarizer.py       # 文章要約
    ├── title_gen.py        # タイトル生成
    ├── proofreader.py      # 文章校正
    ├── catchphrase.py      # キャッチコピー生成
    ├── sns_post.py         # SNS 投稿文生成
    ├── translator.py       # 翻訳
    └── brainstorm.py       # ブレインストーミング
```

---

## セットアップ

### 1. 仮想環境を有効化

```powershell
.venv\Scripts\Activate.ps1
```

### 2. 依存パッケージをインストール

```powershell
pip install -r requirements.txt
```

### 3. API キーを設定

`.env` ファイルを編集して Gemini API キーを入力します。

```env
GEMINI_API_KEY=AIza...（取得したキーを貼り付け）
```

> Gemini API キーは [Google AI Studio](https://aistudio.google.com/) から無料で取得できます。

---

## 起動方法

```powershell
.venv\Scripts\streamlit run app.py
```

ブラウザで `http://localhost:8501` を開くとアプリが表示されます。

> API キーは `.env` に書かず、サイドバーの「Gemini API キー」欄に直接入力することもできます。

---

## 使い方

1. 左サイドバーから使いたいツールを選択する
2. 各フォームに必要な情報を入力する
3. 生成ボタンを押す
4. 結果が画面下に表示される（「📥 テキストをダウンロード」で保存可）
