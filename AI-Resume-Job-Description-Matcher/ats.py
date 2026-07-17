import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

SKILLS = [
    "python",
    "java",
    "c",
    "c++",
    "sql",
    "mysql",
    "mongodb",
    "html",
    "css",
    "javascript",
    "react",
    "node",
    "express",
    "git",
    "github",
    "docker",
    "kubernetes",
    "aws",
    "azure",
    "machine learning",
    "deep learning",
    "nlp",
    "streamlit",
    "langchain",
    "langgraph",
    "tensorflow",
    "pytorch",
    "pandas",
    "numpy",
    "scikit-learn",
    "rag",
    "llm",
    "genai"
]


def ats_score(resume_text, jd_text):
    vectorizer = TfidfVectorizer()

    vectors = vectorizer.fit_transform(
        [resume_text.lower(), jd_text.lower()]
    )

    similarity = cosine_similarity(vectors[0], vectors[1])[0][0]

    return round(similarity * 100, 2)


def extract_skills(text):
    text = text.lower()

    found = []

    for skill in SKILLS:
        if re.search(r"\b" + re.escape(skill) + r"\b", text):
            found.append(skill)

    return found


def compare_skills(resume_text, jd_text):

    resume_skills = set(extract_skills(resume_text))

    jd_skills = set(extract_skills(jd_text))

    matched = sorted(list(resume_skills & jd_skills))

    missing = sorted(list(jd_skills - resume_skills))

    return matched, missing