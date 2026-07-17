import os

from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage

load_dotenv()

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.3,
    api_key=os.getenv("GROQ_API_KEY")
)


def get_feedback(resume, jd):

    prompt = f"""
You are an ATS Resume Expert.

Compare the resume with the job description.

Return your answer in markdown.

Include:

1. ATS Review

2. Resume Strengths

3. Resume Weaknesses

4. Missing Skills

5. Suggestions to improve ATS score

6. Final Rating out of 10

Resume:

{resume}

Job Description:

{jd}
"""

    response = llm.invoke(
        [
            HumanMessage(content=prompt)
        ]
    )

    return response.content