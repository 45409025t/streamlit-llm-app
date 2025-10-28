import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

def get_expert_response(user_input, expert_type):
    system_messages = {
        "医者": "あなたは優秀な医者です。患者の症状を理解し、適切なアドバイスを提供してください。",
        "弁護士": "あなたは経験豊富な弁護士です。法律に関する質問に対して明確で正確な回答を提供してください。",
        "エンジニア": "あなたは熟練したソフトウェアエンジニアです。技術的な問題に対して実用的な解決策を提案してください。"
    }

    system_message = SystemMessage(content=system_messages.get(expert_type))

    chat = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0,
        api_key=api_key
    )

    messages = [
        system_message,
        HumanMessage(content=user_input)
    ]

    response = chat.invoke(messages)
    return response.content

st.title("専門家チャットアプリ")
st.write("このアプリでは、医者、弁護士、エンジニアの専門家として振る舞うAIに質問できます。")

user_input = st.text_area("質問を入力してください:")
expert_type = st.radio("専門家の種類を選択してください:", ("医者", "弁護士", "エンジニア"))

if st.button("送信"):
    if user_input.strip() == "":
        st.warning("質問を入力してください。")
    else:
        response = get_expert_response(user_input, expert_type)
        st.subheader("回答:")
        st.write(response)
