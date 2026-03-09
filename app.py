import streamlit as st

from summarizer import summarize
from quiz_generator import generate_questions
from medical_analyzer import analyze_medical
from legal_analyzer import analyze_legal
from classifier import classify

from utils.pdf_reader import read_pdf
from utils.ppt_reader import read_ppt

st.title("OmniStudy AI")

file = st.file_uploader(
"Upload PDF or PPT",
type=["pdf","pptx"]
)

if file:

    if file.name.endswith(".pdf"):
        text = read_pdf(file)

    else:
        text = read_ppt(file)

    category = classify(text)

    st.write("Detected type:", category)

    if "notes" in category:

        summary = summarize(text)

        st.subheader("Summary")
        st.write(summary)

        questions = generate_questions(summary)

        st.subheader("Quiz Questions")
        st.write(questions)

    elif "medical" in category:

        result = analyze_medical(text)

        st.write(result)

    elif "legal" in category:

        result = analyze_legal(text)

        st.write(result)