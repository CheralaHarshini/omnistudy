import streamlit as st
import pdfplumber
from pptx import Presentation
from transformers import pipeline

st.title("OmniStudy AI")
st.write("Upload a PDF or PPT to get summary and important questions.")

# Load model (without cache first to avoid error)
summarizer = pipeline(
    "text2text-generation",
    model="google/flan-t5-small"
)

def read_pdf(file):
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            content = page.extract_text()
            if content:
                text += content
    return text


def read_ppt(file):
    text = ""
    prs = Presentation(file)
    for slide in prs.slides:
        for shape in slide.shapes:
            if hasattr(shape, "text"):
                text += shape.text
    return text


def summarize(text):
    text = text[:1500]
    prompt = "Summarize this study material: " + text
    result = summarizer(prompt, max_length=120)
    return result[0]["generated_text"]


def generate_questions(text):
    prompt = "Generate 5 important exam questions from this topic: " + text
    result = summarizer(prompt, max_length=120)
    return result[0]["generated_text"]


file = st.file_uploader("Upload PDF or PPT", type=["pdf", "pptx"])

if file:

    if file.name.endswith(".pdf"):
        text = read_pdf(file)
    else:
        text = read_ppt(file)

    st.subheader("Summary")

    summary = summarize(text)
    st.write(summary)

    st.subheader("Important Questions")

    questions = generate_questions(summary)
    st.write(questions)
