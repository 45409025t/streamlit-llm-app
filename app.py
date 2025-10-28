# 画面に入力フォームを1つ用意し、入力フォームから送信したテキストをLangChainを使ってLLMにプロンプトとして渡し、回答結果が画面上に表示されるようにしてください。なお、当コースのLesson8を参考にLangChainのコードを記述してください。
# ラジオボタンでLLMに振る舞わせる専門家の種類を選択できるようにし、Aを選択した場合はAの領域の専門家として、またBを選択した場合はBの領域の専門家としてLLMに振る舞わせるよう、選択値に応じてLLMに渡すプロンプトのシステムメッセージを変えてください。また用意する専門家の種類はご自身で考えてください。
# 「入力テキスト」と「ラジオボタンでの選択値」を引数として受け取り、LLMからの回答を戻り値として返す関数を定義し、利用してください。
# Webアプリの概要や操作方法をユーザーに明示するためのテキストを表示してください。
# Streamlit Community Cloudにデプロイする際、Pythonのバージョンは「3.11」としてください。

import streamlit as st
from langchain.chat_models.openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv
import os

load_dotenv()

def get_expert_response(user_input, expert_type):
    system_messages = {
        "医者": "あなたは優秀な医者です。患者の症状を理解し、適切なアドバイスを提供してください。",
        "弁護士": "あなたは経験豊富な弁護士です。法律に関する質問に対して明確で正確な回答を提供してください。",
        "エンジニア": "あなたは熟練したソフトウェアエンジニアです。技術的な問題に対して実用的な解決策を提案してください。"
    }

    system_message = SystemMessage(content=system_messages.get(expert_type, "あなたは優秀な専門家です。"))

    chat = ChatOpenAI(temperature=0)

    messages = [
        system_message,
        HumanMessage(content=user_input)
    ]

    response = chat(messages)
    return response.content 

st.title("専門家チャットアプリ")
st.write("このアプリでは、医者、弁護士、エンジニアの専門家として振る舞うAIに質問できます。質問内容を入力し、専門家の種類を選択して送信してください。")
user_input = st.text_area("質問を入力してください:")
expert_type = st.radio("専門家の種類を選択してください:", ("医者", "弁護士", "エンジニア"))
if st.button("送信"):
    if user_input.strip() == "":
        st.warning("質問を入力してください。")
    else:
        response = get_expert_response(user_input, expert_type)
        st.subheader("回答:")
        st.write(response)