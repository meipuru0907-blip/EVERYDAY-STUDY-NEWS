import feedparser
import requests
import os
import google.generativeai as genai

# 設定（GitHubのSecretsに保存）
LINE_TOKEN = os.getenv('LINE_TOKEN')
GEMINI_KEY = os.getenv('GEMINI_KEY')

RSS_URLS = [
    "https://www.prosoundweb.com/feed/",
    "https://www.audinate.com/feed",
    "https://www.snrec.jp/feed" # 好きなだけ追加
]

def main():
    # 1. RSSから記事を収集
    entries = []
    for url in RSS_URLS:
        d = feedparser.parse(url)
        entries.extend([f"{e.title}: {e.link}" for e in d.entries[:3]])

    # 2. Geminiで要約
    genai.configure(api_key=GEMINI_KEY)
    model = genai.GenerativeModel('gemini-1.5-flash')
    prompt = "PAエンジニア向けに、以下の記事からギークな5選を日本語で3行要約してURLと送って。\n\n" + "\n".join(entries)
    response = model.generate_content(prompt)
    
    # 3. LINEに送信
    headers = {"Authorization": f"Bearer {LINE_TOKEN}"}
    data = {"messages": [{"type": "text", "text": response.text}]}
    requests.post("https://api.line.me/v2/bot/message/broadcast", headers=headers, json=data)

if __name__ == "__main__":
    main()