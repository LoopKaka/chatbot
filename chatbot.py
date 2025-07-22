from dotenv import load_dotenv
from openai import OpenAI
import streamlit as st

load_dotenv()
client = OpenAI()

st.title("Loop Kaka's Chatbot")

# SYSTEM_PROMPT = """
#     You are a Python AI export.
#     You solve queries on python.
#     If anyone as question not related 
#     to python please tail them to ask python related queries only
# """

if 'messages' not in st.session_state:
    st.session_state.messages = []

# Show Chat History
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# st.session_state.messages.append(
#     {"role": "system", "content": SYSTEM_PROMPT}
# )

user_input = st.chat_input("Apka Query Likiye..")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.write(user_input)

    with st.spinner("Loading"):
        response = client.responses.create(
            model="gpt-4.1-mini",
            input=st.session_state.messages
        )

        st.session_state.messages.append({"role": "assistant", "content": response.output_text})
        with st.chat_message("assistant"):
            st.write(response.output_text)

