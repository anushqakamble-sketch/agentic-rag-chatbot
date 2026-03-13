# app/ui/streamlit_app.py
import requests
import streamlit as st

st.title("Agentic RAG Chatbot")
st.write("Ask anything! PDF content queries will automatically return summaries.")

user_input = st.chat_input("Ask something")

if user_input:
    # Show the user's message
    with st.chat_message("user"):
        st.write(user_input)

    try:
        response = requests.get(
            "http://127.0.0.1:8000/ask",
            params={"query": user_input},
            timeout=300
        )
        if response.status_code == 200:
            result = response.json().get("answer", "No answer found")
        else:
            result = "API error"
    except Exception as e:
        result = f"Error: {e}"

    # Show the assistant's response
    with st.chat_message("assistant"):
        st.write(result)