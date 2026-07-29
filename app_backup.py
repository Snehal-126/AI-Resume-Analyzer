import streamlit as st

from utils.parser import ResumeParser
from utils.preprocess import ResumePreprocessor
from utils.skills import SkillExtractor

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
    preprocessor = ResumePreprocessor()
    skill_extractor = SkillExtractor()

    try:

        resume_text = parser.extract_text(uploaded_resume)
        processed_text, tokens = preprocessor.preprocess(resume_text)
        skills = skill_extractor.extract_skills(processed_text)

        st.success("Resume Uploaded Successfully ✅")

        st.subheader("Original Resume")

        st.text_area(
            "Original",
            resume_text,
            height=250
        )

        st.subheader("Processed Resume")

        st.text_area(
            "Processed",
            processed_text,
            height=250
        )

        st.subheader("Extracted Skills")

        if skills:

             st.success(f"{len(skills)} Skills Found")

             for skill in skills:

              st.write(f"✅ {skill}")

        else:

         st.warning("No Skills Found")

    except Exception as e:

        st.error(e)            #4 setup