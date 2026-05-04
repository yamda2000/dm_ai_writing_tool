# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## コマンド

```powershell
# アプリ起動
.venv\Scripts\streamlit run app.py

# パッケージ追加後
.venv\Scripts\pip install -r requirements.txt

# 構文チェック（例）
.venv\Scripts\python -c "import ast; ast.parse(open('app.py', encoding='utf-8').read()); print('OK')"
```

## アーキテクチャ

シングルページの Streamlit アプリ。ルーティングは `app.py` 内の `TOOLS` dict と `if/elif` チェーンで実装されており、サイドバーの `st.radio` 選択値でレンダリングするセクションを切り替える。Streamlit のマルチページ機能（`pages/` ディレクトリ）は使用していない。

### データフロー

```
app.py（UI・入力収集）
  └─ tools/*.py（プロンプト組み立て）
       └─ utils/gemini_client.generate()（API 呼び出し）
            └─ Google Gemini API
```

各 `tools/*.py` は引数からプロンプト文字列を組み立てて `generate()` に渡すだけで、状態を持たない純粋関数。

### API キーの解決順序

`utils/gemini_client.py` の `get_model()` は `os.getenv("GEMINI_API_KEY")` を参照する。`app.py` のサイドバーで入力された値は `os.environ` に直接セットされるため、`.env` よりもサイドバー入力が優先される（`load_dotenv()` は起動時に一度だけ実行される）。

## 新しいツールを追加するには

1. `tools/` に新モジュールを作成し、`generate()` を呼ぶ関数を実装する
2. `app.py` の `TOOLS` dict にエントリを追加する
3. `app.py` 末尾の `if/elif` チェーンに対応する UI セクションを追加する

## 注意点

- `app.py` は `sys.path.insert(0, os.path.dirname(__file__))` でプロジェクトルートをパスに追加しているため、`tools/` と `utils/` はルート相対でインポートできる
- デフォルトモデルは `gemini-1.5-flash`。`generate()` の `model_name` 引数で変更可能
- テストフレームワーク・リンター・CI は未設定
