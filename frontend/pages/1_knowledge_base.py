import os

import requests
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

TRAINING_DATA_URL = os.getenv("TRAINING_DATA_URL")

st.set_page_config(page_title="knowledge base", page_icon="📈")

st.markdown("# Knowledge Base")
response = requests.get(TRAINING_DATA_URL)
st.markdown(response.json()["data"])

st.title("Knowledge Base Input")

question = st.text_input("Enter the question:")
answer = st.text_area("Enter the answer:")

if st.button("Send Data"):
    if question and answer:
        data = {
            "text": f"{question}\n\n{answer}",
        }
        response = requests.post(TRAINING_DATA_URL, json=data)
        
        if response.status_code == 200:
            response_data = response.json()
            if 'data' in response_data:
                st.markdown("### Response Data")
                st.markdown(response_data["data"])
            else:
                st.error("No 'data' field in the response.")
        else:
            st.error(f"Failed to send data. Status code: {response.status_code}")
    else:
        st.error("Please enter both a question and an answer.")
