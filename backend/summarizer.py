import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel(model_name="models/gemini-2.5-pro")

def generate_summary(text):
    prompt = f"Summarize the following document in less than 150 words:\n\n{text[:4000]}"
    response = model.generate_content(prompt)
    return response.text
