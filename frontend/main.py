import streamlit as st
import requests

st.title("RL Chatbot Agent")

msg = st.text_input("Enter message:")

if st.button("Send"):
    response = requests.post("http://127.0.0.1:8000/chat", json={"text": msg})
    st.write(response.json()["reply"])
