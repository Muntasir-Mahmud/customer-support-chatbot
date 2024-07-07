import os

import requests
import streamlit as st
from dotenv import load_dotenv
from utils import generate_session_id

load_dotenv()

CHATBOT_URL = os.getenv("CHATBOT_URL")

st.set_page_config(
    page_title="chatbot",
    page_icon="🤖",
)


st.title("Customer Support Chatbot")
st.info(
    """I am a customer support agent of Stellar!"""
)

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        if "output" in message.keys():
            st.markdown(message["output"])

        if "explanation" in message.keys():
            with st.status("How was this generated", state="complete"):
                st.info(message["explanation"])

if prompt := st.chat_input("What do you want to know?"):
    st.chat_message("user").markdown(prompt)

    if 'session_id' not in st.session_state:
        st.session_state['session_id'] = generate_session_id()

    st.session_state.messages.append({"role": "user", "output": prompt})

    data = {"text": prompt, "session_id": st.session_state["session_id"]}

    with st.spinner("Waiting for an answer..."):

        response = requests.post(CHATBOT_URL, json=data)

        if response.status_code == 200:
            output_text = response.json()["output"]

        else:
            output_text = """An error occurred while processing your message.
            Please try again or rephrase your message."""
        explanation = output_text

    st.chat_message("assistant").markdown(output_text)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "output": output_text,
        }
    )
