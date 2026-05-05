import streamlit as st
import sys
import os

sys.path.insert(0, os.path.dirname(__file__))

from utils.gemini_client import set_session_api_key

# Streamlit Cloud の secrets からセッションキーをセット
if "GEMINI_API_KEY" in st.secrets:
    set_session_api_key(st.secrets["GEMINI_API_KEY"])

from tools.article import write_article
from tools.email_reply import reply_email
from tools.summarizer import summarize
from tools.title_gen import generate_titles
from tools.proofreader import proofread
from tools.catchphrase import generate_catchphrases
from tools.sns_post import generate_sns_post
from tools.translator import translate
from tools.brainstorm import brainstorm

st.set_page_config(
    page_title="AI ライティングツール",
    page_icon="✍️",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown("""
<style>
    .main-title { font-size: 2rem; font-weight: bold; color: #1f77b4; margin-bottom: 0.2rem; }
    .sub-title { font-size: 0.95rem; color: #666; margin-bottom: 1.5rem; }
    .result-box {
        background: #f8f9fa;
        border-left: 4px solid #1f77b4;
        padding: 1rem 1.2rem;
        border-radius: 4px;
        white-space: pre-wrap;
        font-size: 0.95rem;
        line-height: 1.7;
    }
    .stButton>button {
        background-color: #1f77b4;
        color: white;
        border: none;
        padding: 0.5rem 2rem;
        border-radius: 4px;
        font-size: 1rem;
    }
    .stButton>button:hover { background-color: #1558a0; }
</style>
""", unsafe_allow_html=True)

TOOLS = {
    "📝 記事執筆": "article",
    "📧 メール返信": "email",
    "📋 文章要約": "summarize",
    "🏷️ タイトル生成": "title",
    "🔍 文章校正": "proofread",
    "💡 キャッチコピー": "catchphrase",
    "📱 SNS投稿文": "sns",
    "🌐 翻訳": "translate",
    "🧠 ブレインストーミング": "brainstorm",
}

with st.sidebar:
    st.markdown("## ✍️ AI ライティングツール")
    st.markdown("---")
    selected_label = st.radio("ツールを選択", list(TOOLS.keys()), label_visibility="collapsed")
    st.markdown("---")
    st.caption("Powered by Google Gemini")

selected = TOOLS[selected_label]


def run_with_spinner(func, *args):
    with st.spinner("生成中..."):
        try:
            return func(*args)
        except ValueError as e:
            st.error(str(e))
            return None
        except Exception as e:
            st.error(f"エラーが発生しました: {e}")
            return None


def show_result(result: str):
    if result:
        st.markdown("### 生成結果")
        st.markdown(f'<div class="result-box">{result}</div>', unsafe_allow_html=True)
        st.download_button("📥 テキストをダウンロード", result, file_name="result.txt", mime="text/plain")


# ── 記事執筆 ──────────────────────────────────────────
if selected == "article":
    st.markdown('<div class="main-title">📝 記事執筆</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-title">テーマや条件を指定してブログ・コラム記事を自動生成します</div>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        theme = st.text_input("テーマ・タイトル *", placeholder="例: リモートワークの生産性を上げる5つの方法")
        tone = st.selectbox("文体・トーン", ["です・ます調（丁寧）", "だ・である調（硬め）", "カジュアル", "専門的"])
        target = st.text_input("ターゲット読者", placeholder="例: 30代会社員")
    with col2:
        length = st.selectbox("文字数", ["短め（500字程度）", "普通（1000字程度）", "長め（2000字程度）"])
        keywords = st.text_input("含めるキーワード", placeholder="例: 生産性, 集中力, タスク管理（カンマ区切り）")
    if st.button("記事を生成する"):
        if not theme:
            st.warning("テーマを入力してください")
        else:
            show_result(run_with_spinner(write_article, theme, length, tone, target, keywords))

# ── メール返信 ────────────────────────────────────────
elif selected == "email":
    st.markdown('<div class="main-title">📧 メール返信</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-title">受信メールを貼り付けて、返信文を自動作成します</div>', unsafe_allow_html=True)
    original = st.text_area("受信メール（貼り付け）*", height=180, placeholder="お世話になっております…")
    col1, col2 = st.columns(2)
    with col1:
        intent = st.text_area("返信の要点・意図 *", height=100, placeholder="例: 打ち合わせの日程を来週木曜14時に承諾する")
        tone = st.selectbox("文体", ["丁寧（ビジネス）", "カジュアル（社内・友人）", "フォーマル（取引先）"])
    with col2:
        your_name = st.text_input("差出人名", placeholder="例: 田中 太郎")
    if st.button("返信文を生成する"):
        if not original or not intent:
            st.warning("受信メールと返信の意図を入力してください")
        else:
            show_result(run_with_spinner(reply_email, original, intent, tone, your_name))

# ── 文章要約 ──────────────────────────────────────────
elif selected == "summarize":
    st.markdown('<div class="main-title">📋 文章要約</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-title">長文を指定した形式・長さで要約します</div>', unsafe_allow_html=True)
    text = st.text_area("要約したい文章 *", height=250, placeholder="ここに文章を貼り付けてください…")
    col1, col2 = st.columns(2)
    with col1:
        style = st.selectbox("スタイル", ["ニュートラル", "わかりやすく", "ビジネス向け"])
    with col2:
        length = st.selectbox("要約の長さ", ["1〜2文", "3〜5文", "箇条書き5点", "200字程度"])
    if st.button("要約する"):
        if not text:
            st.warning("文章を入力してください")
        else:
            show_result(run_with_spinner(summarize, text, style, length))

# ── タイトル生成 ──────────────────────────────────────
elif selected == "title":
    st.markdown('<div class="main-title">🏷️ タイトル生成</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-title">記事・コンテンツの内容から魅力的なタイトル候補を提案します</div>', unsafe_allow_html=True)
    content = st.text_area("記事の内容・テーマ・概要 *", height=150,
                            placeholder="例: リモートワークの生産性向上について、集中力・環境整備・ツール活用の3点を解説する記事")
    col1, col2 = st.columns(2)
    with col1:
        count = st.slider("提案数", 3, 10, 5)
    with col2:
        style = st.selectbox("タイトルのスタイル", ["SEO重視", "インパクト重視", "疑問形", "数字入り", "バランス型"])
    if st.button("タイトルを生成する"):
        if not content:
            st.warning("記事の内容を入力してください")
        else:
            show_result(run_with_spinner(generate_titles, content, count, style))

# ── 文章校正 ──────────────────────────────────────────
elif selected == "proofread":
    st.markdown('<div class="main-title">🔍 文章校正</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-title">誤字脱字の修正や文章表現の改善を行います</div>', unsafe_allow_html=True)
    text = st.text_area("校正したい文章 *", height=220, placeholder="ここに文章を貼り付けてください…")
    mode = st.selectbox("校正モード", ["全体校正", "誤字脱字チェック", "表現改善", "ビジネス文書化"])
    if st.button("校正する"):
        if not text:
            st.warning("文章を入力してください")
        else:
            show_result(run_with_spinner(proofread, text, mode))

# ── キャッチコピー ────────────────────────────────────
elif selected == "catchphrase":
    st.markdown('<div class="main-title">💡 キャッチコピー生成</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-title">商品・サービスのキャッチコピーを複数提案します</div>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        product = st.text_input("商品・サービス名 *", placeholder="例: オンライン英会話スクール")
        target = st.text_input("ターゲット", placeholder="例: 働く30代女性")
    with col2:
        features = st.text_area("特徴・強み *", height=100, placeholder="例: 月額980円、ネイティブ講師、24時間受講可能")
        count = st.slider("提案数", 3, 10, 5)
    if st.button("キャッチコピーを生成する"):
        if not product or not features:
            st.warning("商品名と特徴を入力してください")
        else:
            show_result(run_with_spinner(generate_catchphrases, product, features, target, count))

# ── SNS投稿文 ────────────────────────────────────────
elif selected == "sns":
    st.markdown('<div class="main-title">📱 SNS投稿文生成</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-title">各SNSに最適化した投稿文を3パターン提案します</div>', unsafe_allow_html=True)
    content = st.text_area("投稿したい内容・テーマ *", height=120, placeholder="例: 新商品のコーヒーを発売しました。深煎りでコクが強い味わいです")
    col1, col2, col3 = st.columns(3)
    with col1:
        platform = st.selectbox("プラットフォーム", ["Twitter/X", "Instagram", "Facebook", "LinkedIn", "Threads"])
    with col2:
        tone = st.selectbox("トーン", ["フレンドリー", "プロフェッショナル", "ユーモラス", "感情的・共感重視"])
    with col3:
        hashtag = st.checkbox("ハッシュタグを含める", value=True)
    if st.button("投稿文を生成する"):
        if not content:
            st.warning("投稿内容を入力してください")
        else:
            show_result(run_with_spinner(generate_sns_post, content, platform, tone, hashtag))

# ── 翻訳 ─────────────────────────────────────────────
elif selected == "translate":
    st.markdown('<div class="main-title">🌐 翻訳</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-title">テキストを指定した言語に翻訳します</div>', unsafe_allow_html=True)
    text = st.text_area("翻訳するテキスト *", height=200, placeholder="ここにテキストを入力または貼り付け…")
    col1, col2 = st.columns(2)
    with col1:
        target_lang = st.selectbox("翻訳先言語", [
            "英語", "日本語", "中国語（簡体字）", "中国語（繁体字）",
            "韓国語", "フランス語", "ドイツ語", "スペイン語",
            "イタリア語", "ポルトガル語", "ロシア語", "アラビア語",
        ])
    with col2:
        style = st.selectbox("翻訳スタイル", ["自然な表現", "直訳寄り", "ビジネス向け", "カジュアル"])
    if st.button("翻訳する"):
        if not text:
            st.warning("テキストを入力してください")
        else:
            show_result(run_with_spinner(translate, text, target_lang, style))

# ── ブレインストーミング ──────────────────────────────
elif selected == "brainstorm":
    st.markdown('<div class="main-title">🧠 ブレインストーミング</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-title">テーマに沿ったアイデアを自由に発想します</div>', unsafe_allow_html=True)
    theme = st.text_input("テーマ *", placeholder="例: 従業員のモチベーションを上げる施策")
    col1, col2 = st.columns(2)
    with col1:
        count = st.slider("アイデア数", 5, 20, 10)
    with col2:
        perspective = st.selectbox("視点", [
            "多角的（バランス型）", "ビジネス・経営", "マーケティング",
            "テクノロジー活用", "低コスト・無料でできること", "ユーザー体験（UX）",
        ])
    if st.button("アイデアを出す"):
        if not theme:
            st.warning("テーマを入力してください")
        else:
            show_result(run_with_spinner(brainstorm, theme, count, perspective))
