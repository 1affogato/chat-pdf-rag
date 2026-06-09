import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.set_page_config(
    page_title="Chat PDF RAG",
    page_icon="📝"
)

st.title("📝 Chat PDF RAG")

# Upload

uploaded_file = st.file_uploader(
    "Upload a PDF",
    type=["pdf"]
)

if uploaded_file:

    files = {
        "file": (
            uploaded_file.name,
            uploaded_file,
            "application/pdf"
        )
    }

    if st.button("Upload PDF"):

        response = requests.post(
            f"{API_URL}/upload",
            files=files
        )

        st.success(
            f"Uploaded: {uploaded_file.name}"
        )

# Pregunta

question = st.text_input(
    "Ask a question"
)

if st.button("Send"):

    response = requests.post(
        f"{API_URL}/ask",
        json={
            "question": question
        }
    )

    answer = response.json()["answer"]

    st.markdown("### Answer")

    st.write(answer)