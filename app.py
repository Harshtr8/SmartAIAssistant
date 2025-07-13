# ================= app.py =================
import streamlit as st
from backend.extractor import extract_text_from_pdf, extract_text_from_txt
from backend.summarizer import generate_summary
from backend.qa_engine import prepare_qa_chain, answer_question, generate_logic_questions, evaluate_user_answer

st.set_page_config(page_title="Smart Assistant", layout="wide")
st.title("📚 Smart Assistant for Research Summarization")

uploaded_file = st.file_uploader("Upload your research document (PDF or TXT)", type=["pdf", "txt"])

if uploaded_file:
    if uploaded_file.name.endswith(".pdf"):
        text = extract_text_from_pdf(uploaded_file)
    else:
        text = extract_text_from_txt(uploaded_file)

    st.subheader("📄 Auto Summary")
    summary = generate_summary(text)
    st.success(summary)

    mode = st.radio("Choose Interaction Mode:", ["Ask Anything", "Challenge Me"])

    vectordb = prepare_qa_chain(text)

    if mode == "Ask Anything":
        question = st.text_input("Ask a question based on the document:")
        if question:
            answer = answer_question(question, vectordb)
            st.markdown("**Answer:** " + answer)

    elif mode == "Challenge Me":
        st.info("Below are 3 logic/comprehension questions based on the document. Try answering them!")
        questions = generate_logic_questions(text)
        for idx, q in enumerate(questions):
            st.markdown(f"**Q{idx+1}.** {q}")
            user_ans = st.text_input(f"Your Answer {idx+1}")
            if user_ans:
                feedback = evaluate_user_answer(q, user_ans, text)
                st.markdown(f"🧠 Feedback: {feedback}")
