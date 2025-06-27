import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient
import streamlit as st

# Load .env token
load_dotenv()
hf_token = os.getenv("HF_TOKEN")
client = InferenceClient(token=hf_token)

# Streamlit page config
st.set_page_config(page_title="MiniMax Chatbot", layout="centered")

# Title
st.markdown("<h1 style='text-align: center; color: #333;'>🤖 MiniMax Chatbot</h1>", unsafe_allow_html=True)
st.markdown("---")

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Chat display area (top)
chat_container = st.container()
with chat_container:
    for msg in st.session_state.chat_history:
        if msg["role"] == "user":
            st.markdown(
                f"""
                <div style='
                    text-align: right;
                    background-color: #d1e7ff;
                    color: #0b2545;
                    padding: 10px;
                    margin: 8px;
                    border-radius: 12px;
                    max-width: 75%;
                    margin-left: auto;
                    box-shadow: 2px 2px 5px rgba(0,0,0,0.1);
                    font-size: 16px;
                '>
                    <b>You:</b> {msg['content']}
                </div>
                """,
                unsafe_allow_html=True,
            )
        else:
            st.markdown(
                f"""
                <div style='
                    text-align: left;
                    background-color: #c8f7c5;
                    color: #1b5e20;
                    padding: 10px;
                    margin: 8px;
                    border-radius: 12px;
                    max-width: 75%;
                    margin-right: auto;
                    box-shadow: 2px 2px 5px rgba(0,0,0,0.1);
                    font-size: 16px;
                '>
                    <b>Bot:</b> {msg['content']}
                </div>
                """,
                unsafe_allow_html=True,
            )

st.markdown("---")

# Bottom input box
with st.container():
    with st.form(key="chat_form", clear_on_submit=True):
        user_input = st.text_input("Type your message:", "")
        submitted = st.form_submit_button("Send")

        if submitted and user_input.strip():
            # Append user message
            st.session_state.chat_history.append({"role": "user", "content": user_input})

            # Get bot reply
            with st.spinner("Thinking..."):
                response = client.chat_completion(
                    model="MiniMaxAI/MiniMax-M1-80k",
                    messages=st.session_state.chat_history,
                    temperature=0.7,
                )
                bot_reply = response.choices[0].message.content

            # Append bot message
            st.session_state.chat_history.append({"role": "assistant", "content": bot_reply})

            # Rerun to update chat display immediately
            st.rerun()
