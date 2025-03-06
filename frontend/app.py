import streamlit as st
import requests
from fpdf import FPDF

BACKEND_URL = "http://127.0.0.1:8000"

st.title("AI-Powered Quiz Generator")
st.write("Enter a text or upload a PDF to generate MCQs!")

text_input = st.text_area("Enter text for MCQs:", "")

uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])

if uploaded_file:
    files = {"file": uploaded_file.getvalue()}
    response = requests.post(f"{BACKEND_URL}/upload_pdf/", files=files)
    if response.status_code == 200:
        text_input = response.json()["text"]
        st.success("Text extracted from PDF!")

if st.button("Generate Quiz"):
    if text_input:
        response = requests.post(f"{BACKEND_URL}/generate_quiz/", json={"text": text_input})
        if response.status_code == 200:
            mcqs = response.json()["mcqs"]
            st.session_state["mcqs"] = mcqs  # Store MCQs in session state
            st.success("Quiz Generated!")
        else:
            st.error("Failed to generate quiz. Try again.")

if "mcqs" in st.session_state:
    st.subheader("Generated MCQs:")
    for i, mcq in enumerate(st.session_state["mcqs"], 1):
        st.write(f"**{i}.** {mcq['question']}")
        st.write(f"Options: {', '.join(mcq['options'])}")
        st.write(f"Answer: {mcq['answer']}")
        st.write("---")

def create_pdf(mcqs):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt="Generated Quiz", ln=True, align="C")
    pdf.ln(10)

    for i, mcq in enumerate(mcqs, 1):
        pdf.multi_cell(0, 10, f"{i}. {mcq['question']}")
        pdf.multi_cell(0, 10, f"Options: {', '.join(mcq['options'])}")
        pdf.multi_cell(0, 10, f"Answer: {mcq['answer']}")
        pdf.ln(5)

    pdf_path = "generated_quiz.pdf"
