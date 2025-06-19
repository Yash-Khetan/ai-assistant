import uuid
import time
import csv
from datetime import datetime

# Generate a session ID once per user visit
if "session_id" not in st.session_state:
    st.session_state["session_id"] = str(uuid.uuid4())[:8]

def log_session_interaction():
    timestamp = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    session_id = st.session_state["session_id"]

    with open("usage_log.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([session_id, timestamp])

import streamlit as st
from PyPDF2 import PdfReader
from transformers import pipeline

# Load model (only once)
@st.cache_resource
def load_model():
    return pipeline("text2text-generation", model="google/flan-t5-base")

qa_pipeline = load_model()

# Extract text from uploaded PDF
def extract_text_from_pdf(uploaded_file):
    reader = PdfReader(uploaded_file)
    if (len(reader.pages) > 2):
        st.error("Greater than max limit!! Upload a pdf of 2 page only! -- re upload")
        st.stop()
    text = ""
    for page in reader.pages:
        
        text += page.extract_text()
    return text

# Ask question using LLM
def ask_question(question, context):
    prompt = f"Answer the question based only on the brochure below:\n\nBrochure:\n{context}\n\nQuestion: {question}"
    result = qa_pipeline(prompt, max_length=200)[0]['generated_text']
    return result

# UI
st.set_page_config(page_title="PDF QA", layout="centered")
st.markdown("⚠️ *This tool is for demo use only. Do not upload confidential documents.*")

st.title("PDF Assistant")

uploaded_file = st.file_uploader("Upload a PDF", type="pdf")

if uploaded_file:
    brochure_text = extract_text_from_pdf(uploaded_file)
    st.success("✅ PDF uploaded and processed!")

    question = st.text_input("Ask a question about the PDF:")
    
    if question:
        log_session_interaction()
        with st.spinner("🤖 Thinking..."):
            answer = ask_question(question, brochure_text)
        st.markdown("### 🧠 Answer:")
        st.write(answer)
else:
    st.info("👆 Upload a PDF to get started(2 pages max).")
