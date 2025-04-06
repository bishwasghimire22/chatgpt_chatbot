import streamlit as st
from chatbot.pdf_reader import extract_text_from_pdf
from chatbot.vector_store import create_vector_store
from chatbot.chat_engine import create_qa_chain
import tempfile

st.set_page_config(page_title="Chat with PDF", layout="centered")
st.title("Chat with your PDF (Smart Search)")

uploaded_file = st.file_uploader("Upload a PDF", type="pdf")
if uploaded_file:
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        tmp_file.write(uploaded_file.read())
        tmp_path = tmp_file.name

    pdf_text = extract_text_from_pdf(tmp_path)
    vector_store = create_vector_store(pdf_text)
    qa_chain = create_qa_chain(vector_store)

    question = st.text_input("Ask a question about the PDF")
    if question:
        with st.spinner("Searching and thinking..."):
            answer = qa_chain.run(question)
        st.markdown("**Answer:**")
        st.write(answer)
