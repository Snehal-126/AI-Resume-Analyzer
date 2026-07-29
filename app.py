import streamlit as st

from utils.parser import ResumeParser
from utils.preprocess import ResumePreprocessor
from utils.skills import SkillExtractor
from utils.similarity import ResumeMatcher
from utils.ats import ATSAnalyzer
from utils.pdf_report import PDFReport
from utils.charts import ChartGenerator
from utils.database import ResumeDatabase

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

# ---------------- Sidebar ---------------- #

st.sidebar.title("📄 AI Resume Analyzer")

st.sidebar.markdown("---")

st.sidebar.info("""
### Features

✅ Resume Upload

✅ Skill Extraction

✅ Resume Match Score

✅ ATS Score

✅ Dashboard

✅ PDF Report

✅ Database History
""")

st.sidebar.markdown("---")

st.sidebar.success(
    "Developed using Python, NLP & Machine Learning"
)

# ---------------- Header ---------------- #

st.title("📄 AI Resume Analyzer")

st.caption("Analyze resumes with AI-powered insights")

st.markdown("---")

# ---------------- Input Section ---------------- #

col1, col2 = st.columns(2)

with col1:

    uploaded_resume = st.file_uploader(
        "📂 Upload Resume",
        type=["pdf", "docx"]
    )

with col2:

    job_description = st.text_area(
        "💼 Paste Job Description",
        height=200
    )

analyze = st.button(
    "🚀 Analyze Resume",
    use_container_width=True
)

# ---------------- Main Logic ---------------- #

if uploaded_resume is not None:

    parser = ResumeParser()
    preprocessor = ResumePreprocessor()
    skill_extractor = SkillExtractor()
    matcher = ResumeMatcher()
    ats = ATSAnalyzer()
    pdf = PDFReport()
    chart = ChartGenerator()
    database = ResumeDatabase()

    try:

        resume_text = parser.extract_text(uploaded_resume)

        processed_text, resume_tokens = preprocessor.preprocess(
            resume_text
        )

        resume_skills = skill_extractor.extract_skills(
            processed_text
        )

        st.success("Resume Uploaded Successfully ✅")

        with st.expander("📄 View Original Resume"):

            st.text_area(
                "",
                resume_text,
                height=220
            )

        with st.expander("🧹 View Processed Resume"):

            st.text_area(
                "",
                processed_text,
                height=220
            )

        st.subheader("🛠 Extracted Skills")

        if resume_skills:

            for skill in resume_skills:
                st.success(skill)

        else:

            st.warning("No skills detected.")

        # ---------------- Analysis ---------------- #

        if analyze:

            if job_description.strip() == "":

                st.warning(
                    "Please paste a Job Description."
                )

            else:

                processed_job, job_tokens = preprocessor.preprocess(
                    job_description
                )

                job_skills = skill_extractor.extract_skills(
                    processed_job
                )

                match_score = matcher.calculate_similarity(
                    processed_text,
                    processed_job
                )

                matching_skills = sorted(
                    list(
                        set(resume_skills).intersection(
                            set(job_skills)
                        )
                    )
                )

                missing_skills = sorted(
                    list(
                        set(job_skills) -
                        set(resume_skills)
                    )
                )

                ats_score = ats.calculate_ats_score(
                    match_score,
                    len(resume_skills),
                    len(job_skills)
                )

                database.insert_record(
                    uploaded_resume.name,
                    match_score,
                    ats_score
                )

                st.markdown("---")

                metric1, metric2 = st.columns(2)

                with metric1:

                    st.metric(
                        "📊 Resume Match",
                        f"{match_score}%"
                    )

                with metric2:

                    st.metric(
                        "🎯 ATS Score",
                        f"{ats_score}%"
                    )

                st.progress(ats_score / 100)

                col1, col2 = st.columns(2)

                with col1:

                    st.subheader("✅ Matching Skills")

                    if matching_skills:

                        for skill in matching_skills:
                            st.success(skill)

                    else:

                        st.warning("No matching skills.")

                with col2:

                    st.subheader("❌ Missing Skills")

                    if missing_skills:

                        for skill in missing_skills:
                            st.error(skill)

                    else:

                        st.success("No missing skills.")
                                        # ---------------- Resume Suggestions ---------------- #

                st.markdown("---")
                st.subheader("💡 Resume Suggestions")

                suggestions = []

                if missing_skills:
                    suggestions.append(
                        "Add the missing skills if you have practical experience with them."
                    )

                if match_score < 70:
                    suggestions.append(
                        "Customize your resume according to the Job Description."
                    )

                if ats_score < 75:
                    suggestions.append(
                        "Improve your ATS score by adding more relevant technical keywords."
                    )

                if len(resume_skills) < 5:
                    suggestions.append(
                        "Include more technical skills and projects in your resume."
                    )

                if suggestions:

                    for suggestion in suggestions:
                        st.info(suggestion)

                else:

                    st.success(
                        "🎉 Excellent! Your resume is well optimized."
                    )

                # ---------------- Dashboard ---------------- #

                st.markdown("---")

                st.subheader("📊 Dashboard Analytics")

                chart_col1, chart_col2 = st.columns(2)

                with chart_col1:

                    score_fig = chart.score_chart(
                        match_score,
                        ats_score
                    )

                    st.pyplot(score_fig)

                with chart_col2:

                    skill_fig = chart.skill_chart(
                        len(matching_skills),
                        len(missing_skills)
                    )

                    st.pyplot(skill_fig)

                # ---------------- PDF Report ---------------- #

                pdf.generate_report(
                    "Resume_Report.pdf",
                    match_score,
                    ats_score,
                    resume_skills,
                    matching_skills,
                    missing_skills
                )

                with open("Resume_Report.pdf", "rb") as pdf_file:

                    st.download_button(
                        label="📥 Download PDF Report",
                        data=pdf_file,
                        file_name="Resume_Report.pdf",
                        mime="application/pdf"
                    )

                # ---------------- Database History ---------------- #

                st.markdown("---")

                st.subheader("📂 Analysis History")

                records = database.get_records()

                if records:

                    history = []

                    for row in records:

                        history.append(
                            {
                                "Resume": row[0],
                                "Match Score": row[1],
                                "ATS Score": row[2],
                                "Date": row[3]
                            }
                        )

                    st.dataframe(
                        history,
                        use_container_width=True
                    )

                else:

                    st.info("No analysis history found.")

    except Exception as e:

        st.error(f"Error: {e}")

# ---------------- Footer ---------------- #

st.markdown("---")

st.caption(
    "Made with ❤️ using Python, Streamlit, spaCy, Scikit-learn, Matplotlib and SQLite"
)