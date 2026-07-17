import streamlit as st

from parser import extract_pdf, extract_docx
from ats import ats_score, compare_skills
from ai_feedback import get_feedback

st.set_page_config(
    page_title="Resume vs Job Description Matcher",
    page_icon="📄",
    layout="wide"
)

st.title("📄 AI Resume vs Job Description Matcher")

resume = st.file_uploader(
    "Upload Resume",
    type=["pdf", "docx"]
)

jd = st.text_area(
    "Paste Job Description",
    height=250
)

resume_text = ""

if resume:

    if resume.name.endswith(".pdf"):
        resume_text = extract_pdf(resume)
    else:
        resume_text = extract_docx(resume)

    st.success("Resume Uploaded Successfully!")

    with st.expander("Resume Preview"):
        st.write(resume_text)

if st.button("Analyze Resume"):

    if resume is None:
        st.error("Please upload your resume.")
        st.stop()

    if jd.strip() == "":
        st.error("Please paste the Job Description.")
        st.stop()

    score = ats_score(resume_text, jd)

    matched, missing = compare_skills(resume_text, jd)

    st.subheader("📊 ATS Score")

    st.progress(int(score))

    st.metric("Match Percentage", f"{score}%")

    col1, col2 = st.columns(2)

    with col1:
        st.success("✅ Matching Skills")

        if matched:
            for skill in matched:
                st.write(f"• {skill}")
        else:
            st.write("No matching skills found.")

    with col2:
        st.error("❌ Missing Skills")

        if missing:
            for skill in missing:
                st.write(f"• {skill}")
        else:
            st.write("No missing skills.")

    st.divider()

    st.subheader("🤖 AI Feedback")

    with st.spinner("Analyzing Resume..."):

        feedback = get_feedback(resume_text, jd)

    st.markdown(feedback)