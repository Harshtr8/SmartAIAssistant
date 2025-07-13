import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel(model_name="models/gemini-1.5-flash")


from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings # used for FAISS
from langchain.docstore.document import Document

def prepare_qa_chain(text):
    splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=150)
    chunks = splitter.split_text(text)
    docs = [Document(page_content=chunk) for chunk in chunks]
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    vectordb = FAISS.from_documents(docs, embeddings)
    return vectordb

def answer_question(question, vectordb):
    relevant_docs = vectordb.similarity_search(question, k=3)
    context = "\n".join([doc.page_content for doc in relevant_docs])
    prompt = f"Use the following context to answer the question.\n\nContext:\n{context}\n\nQuestion: {question}"
    response = model.generate_content(prompt)
    return response.text

def generate_logic_questions(text):
    prompt = f"Generate 3 logic-based or comprehension-focused questions from this document:\n\n{text[:4000]}"
    response = model.generate_content(prompt)
    return response.text.strip().split("\n")

def evaluate_user_answer(question, user_answer, text):
    prompt = f"""
Evaluate the user's answer.

Question: {question}
User's Answer: {user_answer}

Based on the following context:
{text[:4000]}

Is the answer correct? Justify in 1-2 sentences.
"""
    response = model.generate_content(prompt)
    return response.text
