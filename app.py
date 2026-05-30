import os
import platform

# Redirect HF cache to D: drive locally on Windows to prevent C: drive running out of space
if platform.system() == "Windows" and os.path.exists("D:\\"):
    os.environ["HF_HOME"] = "D:/huggingface"

import streamlit as st
import PyPDF2
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# Load summarization model (cached after first run)
@st.cache_resource
def load_model():
    model_name = "facebook/bart-large-cnn"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
    return tokenizer, model

tokenizer, model = load_model()

def extract_text_from_pdf(file):
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page in reader.pages:
        if page.extract_text():
            text += page.extract_text()
    return text

def split_text(text, max_chunk_size=1000):
    paragraphs = text.split('\n')
    chunks, current_chunk = [], ""
    for para in paragraphs:
        if len(current_chunk) + len(para) < max_chunk_size:
            current_chunk += para + "\n"
        else:
            chunks.append(current_chunk.strip())
            current_chunk = para + "\n"
    if current_chunk:
        chunks.append(current_chunk.strip())
    return chunks

def summarize_text(text):
    chunks = split_text(text)
    summaries = []
    for chunk in chunks:
        inputs = tokenizer(chunk, max_length=1024, truncation=True, return_tensors="pt")
        summary_ids = model.generate(inputs["input_ids"], max_length=150, min_length=40, do_sample=False)
        summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
        summaries.append(summary)
    return "\n\n".join(summaries)


# Streamlit UI
st.title("🧠 AI Notes Maker")

input_method = st.radio("Choose input method:", ["Paste Text", "Upload PDF"])
user_input = ""

if input_method == "Paste Text":
    user_input = st.text_area("Paste your content below:")
elif input_method == "Upload PDF":
    uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])
    if uploaded_file:
        user_input = extract_text_from_pdf(uploaded_file)
        st.success("Text extracted from PDF!")

if st.button("Generate Notes") and user_input.strip():
    with st.spinner("Generating notes..."):
        notes = summarize_text(user_input)
        st.subheader("📋 Generated Notes")
        st.text_area("Your Notes", notes, height=300)
        st.download_button("📥 Download Notes", notes, file_name="notes.txt")
