AI Notes Maker 🧠

A simple and powerful AI-based notes generator that converts long text or PDFs into clean, concise bullet-point notes using state-of-the-art NLP models.

This project runs fully offline using HuggingFace transformer models — perfect for students, researchers, or developers preparing study notes.

🚀 Features

Text Summarization
Paste any long text and get crisp bullet-point notes.

PDF Support
Upload PDFs and automatically extract + summarize content.

Offline AI Model
Uses Hugging Face’s facebook/bart-large-cnn — no API key needed.

Web App UI
Built using Streamlit for a clean, interactive interface.

Download Notes
Save generated notes as a .txt file.

🧠 Tech Stack

Python

Streamlit – web UI

Transformers (Hugging Face) – AI summarization

PyPDF2 – PDF text extraction

📦 Installation
1️⃣ Clone the repository
git clone https://github.com/your-username/ai-notes-maker.git
cd ai-notes-maker

2️⃣ Create & activate a virtual environment (recommended)
python -m venv venv
venv\Scripts\activate   # Windows

3️⃣ Install required libraries
pip install -r requirements.txt


If you don’t have requirements.txt, install manually:

pip install streamlit transformers PyPDF2 sentencepiece

💻 Run the App
streamlit run app.py


App will start at:

http://localhost:8501

📙 How It Works

User pastes text or uploads a PDF

App extracts raw text

AI model (facebook/bart-large-cnn) summarizes it

Output converted into clean bullet points

User downloads .txt notes



                        check out 
              https://rahul-2503-ainotesmaker-app-t7lwid.streamlit.app/
