import streamlit as st
from chatbot import get_groq_response

st.set_page_config(page_title="Chatbot", page_icon=":robot_face:")

st.title("Chat with our AI Chatbot")
st.write("Ask me anything!")

user_input = st.text_input("You: ", "")

if user_input:
    bot_response = get_groq_response(user_input)
    st.write(f"Chatbot: {bot_response}")
