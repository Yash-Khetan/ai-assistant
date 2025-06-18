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
st.set_page_config(page_title="Real Estate Brochure QA", layout="centered")
st.title("🏡 Real Estate Brochure Assistant")

uploaded_file = st.file_uploader("Upload a brochure (PDF)", type="pdf")

if uploaded_file:
    brochure_text = extract_text_from_pdf(uploaded_file)
    st.success("✅ Brochure uploaded and processed!")

    question = st.text_input("Ask a question about the property:")
    
    if question:
        with st.spinner("🤖 Thinking..."):
            answer = ask_question(question, brochure_text)
        st.markdown("### 🧠 Answer:")
        st.write(answer)
else:
    st.info("👆 Upload a property PDF to get started.")
