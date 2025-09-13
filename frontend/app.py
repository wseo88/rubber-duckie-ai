import streamlit as st
import requests

API_URL = "http://localhost:8000/chat"

st.title("LLM Chatbot with Redis")

user_id = st.text_input("Enter your user ID", value="default")
user_message = st.text_input("Enter your message")

if st.button("Send"):
    response = requests.post(API_URL, json={"user_id": user_id, "message": user_message})
    st.write(response.json()["response"])

if st.button("Clear"):
    requests.post(API_URL, json={"user_id": user_id, "message": ""})
    st.write("Conversation cleared")
    