import streamlit as st
import PyPDF2
from transformers import pipeline

# Load summarization model (cached after first run)
@st.cache_resource
def load_model():
    return pipeline("summarization", model="facebook/bart-large-cnn")

summarizer = load_model()

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
        summary = summarizer(chunk, max_length=150, min_length=40, do_sample=False)[0]["summary_text"]
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
