import streamlit as st

from utils.parser import ResumeParser

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

st.title("📄 AI Resume Analyzer")

st.write("Upload your resume below.")

uploaded_resume = st.file_uploader(
    "Upload Resume",
    type=["pdf", "docx"]
)

if uploaded_resume is not None:

    parser = ResumeParser()

    resume_text = parser.extract_text(uploaded_resume)

    st.success("Resume Uploaded Successfully ✅")

    st.subheader("Extracted Resume Text")

    st.text_area(
        "Resume Content",
        resume_text,
        height=400
    )
