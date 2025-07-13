# 🤖 Smart AI Assistant for Research Summarization

This is an AI-powered assistant built using **Google Gemini Pro (2.5)** and **LangChain**, designed to:

✅ Summarize uploaded documents  
✅ Answer free-form questions from the content  
✅ Generate and evaluate logic-based questions  
✅ Justify every answer with document context  

---

## 🔗 Live Demo

[https://smartassistantt.streamlit.app](https://smartassistantt.streamlit.app/)


## 🚀 Features

- 📄 **Document Upload**: Supports PDF and TXT
- ✨ **Auto Summary**: Generates a 150-word summary immediately after upload
- ❓ **Ask Anything Mode**: Ask questions and get accurate answers with context
- 🧠 **Challenge Me Mode**: System asks you logical questions and evaluates your answers
- 📌 **Contextual Justifications**: Every answer is based on retrieved document text
- 💡 **Fully Gemini-powered with HuggingFace Embeddings (OpenAI-free)**

---

## 🛠️ Tech Stack

- Streamlit for UI  
- Google Gemini Pro 2.5 for LLM  
- LangChain for Q&A logic  
- FAISS for local semantic search  
- HuggingFace Embeddings for vector indexing  
- PyMuPDF for PDF parsing  

---

## 📂 Folder Structure

```
smart-assistant/
├── app.py                      # Streamlit UI
├── backend/
│   ├── extractor.py            # Text extraction from PDF/TXT
│   ├── summarizer.py           # Gemini-based summarization
│   └── qa_engine.py            # Q&A + logic questions
├── .env                        # Gemini API key
├── requirements.txt            # All dependencies
└── README.md                   # You're here!
```

---

## 📦 Setup Instructions

### 1. Clone this repo

```bash
git clone https://github.com/sarthak7518/SmartAssistant.git
cd SmartAssistant
```

### 2. Create a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate     # Mac/Linux
.venv\Scripts\activate        # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add your Gemini API Key

Create a `.env` file and add:

```
GEMINI_API_KEY=your_google_api_key_here
```

### 5. Run the app

```bash
streamlit run app.py
```

---

## 🌐 Deploy on Streamlit Cloud

To deploy:
1. Push this project to GitHub
2. Visit: [https://streamlit.io/cloud](https://streamlit.io/cloud)
3. Click **"New app"**
4. Select your repo and deploy!

