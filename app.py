import streamlit as st
import pdfplumber
from pptx import Presentation
from transformers import pipeline

st.title("OmniStudy AI")

@st.cache_resource
def load_model():
    return pipeline("text2text-generation", model="google/flan-t5-small")

model = load_model()

def read_pdf(file):
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            t = page.extract_text()
            if t:
                text += t
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
    prompt = f"Summarize this:\n{text}"
    result = model(prompt, max_length=120)
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
