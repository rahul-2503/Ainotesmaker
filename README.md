# AI Notes Maker 🧠

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_svg.svg)](https://rahul-2503-ainotesmaker-app-t7lwid.streamlit.app/)
[![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Spaces-yellow)](https://huggingface.co/spaces)
[![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

⚡ **Live Demo:** [https://rahul-2503-ainotesmaker-app-t7lwid.streamlit.app/](https://rahul-2503-ainotesmaker-app-t7lwid.streamlit.app/)

AI Notes Maker is an intelligent, privacy-first web application designed to automatically summarize long articles, research papers, and uploaded PDF documents into concise, structured bullet-point notes. 

The application runs **fully offline** utilizing Hugging Face's BART Seq2Seq model, requiring no API keys, and keeping all your data private.

---

## 🚀 Features

- **Text Summarization:** Paste long texts directly and generate structured study notes.
- **PDF Document Support:** Upload any PDF to extract and summarize content.
- **Smart Text Chunking:** Automatically splits long documents into manageable chunks so the AI model can process large datasets without exceeding token limits.
- **Zero API Key Requirement:** Powered locally by the `facebook/bart-large-cnn` model.
- **Downloadable Summaries:** Export your generated notes as a `.txt` file with one click.
- **Modern Responsive UI:** A clean, minimal, and fully interactive interface built with Streamlit.

---

## 🛠️ Technical Stack

- **Frontend & App Framework:** [Streamlit](https://streamlit.io/)
- **Core AI Engine:** [Hugging Face Transformers](https://huggingface.co/docs/transformers/index) (v5+ compatible)
- **AI Model:** `facebook/bart-large-cnn` (BART Seq2Seq LM)
- **Deep Learning Library:** [PyTorch](https://pytorch.org/)
- **PDF Processing:** [PyPDF2](https://pypdf.com/)

---

## 📦 Installation & Local Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/rahul-2503/Ainotesmaker.git
cd Ainotesmaker
```

### 2️⃣ Create & Activate a Virtual Environment
```bash
python -m venv .venv
# On Windows PowerShell:
.venv\Scripts\Activate.ps1
# On macOS/Linux:
source .venv/bin/activate
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

---

## 💾 Running Out of Disk Space locally? (e.g., full C: drive)
The BART model is approximately **1.6 GB**. If your primary system drive (`C:`) has low storage capacity, you can redirect the cache and temporary downloads to another drive (such as `D:`) before installing and running.

#### Option A: Run with custom cache environment variables:
```powershell
# PowerShell (Windows)
$env:TEMP='D:\temp'
$env:TMP='D:\temp'
$env:PIP_CACHE_DIR='D:\pip-cache'
pip install -r requirements.txt
```

#### Option B: Automated Platform Redirection (Built-in)
The application has built-in protection in `app.py` that detects if it is running on a Windows system with a `D:` drive and automatically redirects the HuggingFace cache directory (`HF_HOME`) to `D:/huggingface` to prevent your `C:` drive from running out of space.

---

## 💻 Running the Application

To run the Streamlit application locally, run the following command in your terminal:
```bash
streamlit run app.py
```
Once started, open your web browser and navigate to:
👉 **[http://localhost:8501](http://localhost:8501)**

---

## 🌐 Deploying to the Cloud

### 🎈 Streamlit Community Cloud (Recommended)
This repository is optimized for Streamlit Cloud deployment.
1. Push your latest code changes to your GitHub repository.
2. Sign in to [Streamlit Community Cloud](https://share.streamlit.io/) using your GitHub account.
3. Click **Create app** and select your repository (`rahul-2503/Ainotesmaker`).
4. Set the **Main file path** to `app.py` and click **Deploy**.
5. Live deployment is configured at: [https://rahul-2503-ainotesmaker-app-t7lwid.streamlit.app/](https://rahul-2503-ainotesmaker-app-t7lwid.streamlit.app/)

### 🤗 Hugging Face Spaces
1. Create a new Space on [Hugging Face](https://huggingface.co/new-space).
2. Choose **Streamlit** as the SDK.
3. Push the files to the Space git remote (or link the Space to your GitHub repository).

---

## 📜 License
This project is open-source and licensed under the [MIT License](LICENSE).
