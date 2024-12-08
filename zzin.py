#from dotenv import load_dotenv
#load_dotenv()

from langchain_openai import ChatOpenAI
chat_model = ChatOpenAI()

from langchain_openai import *

import streamlit as st

# Streamlit UI 설정
st.title("인공지능 시인")
subject = st.text_input("시의 주제를 입력해주세요.")

# 사용자가 주제를 입력했을 때
if subject:
    st.write("시의 주제: " + subject)

    # 시 작성 버튼 클릭 시
    if st.button("시 작성"):
        with st.spinner("시 작성중 ..."):
            result = chat_model.invoke(f"'{subject}'를 주제로 시를 작성해줘.")
            st.write(result.content)
