# 📄 AI Resume vs Job Description Matcher

An AI-powered Resume Analyzer built using **Python**, **Streamlit**, **LangChain**, and **Groq LLM**. This application compares a candidate's resume with a job description, calculates an ATS (Applicant Tracking System) score, identifies matching and missing skills, and provides AI-generated feedback to improve the resume.

---

## 🚀 Features

- 📄 Upload Resume (PDF/DOCX)
- 📋 Paste Job Description
- 📊 ATS Match Score
- ✅ Matching Skills Detection
- ❌ Missing Skills Detection
- 🤖 AI-Powered Resume Feedback
- 💡 Resume Improvement Suggestions
- ⚡ Interactive Streamlit User Interface

---

## 🛠️ Tech Stack

- Python
- Streamlit
- LangChain
- LangGraph
- Groq LLM
- Scikit-Learn
- Pandas
- NumPy
- PyPDF2
- python-docx

---

## 📋 Requirements

Before running this project, make sure you have:

- Python 3.10 or above
- pip
- Virtual Environment (Recommended)
- Groq API Key
- Internet Connection

---

## 📦 Installation

### Clone the Repository

```bash
git clone https://github.com/Tushar1752/resume_matcher.git
```

### Go to the Project Folder

```bash
cd resume_matcher
```

### Create Virtual Environment

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Create `.env` File

```env
GROQ_API_KEY=YOUR_GROQ_API_KEY
```

---

## ▶️ Run the Project

```bash
streamlit run app.py
```

---

## 📂 Project Structure

```text
resume_matcher/
│── app.py
│── parser.py
│── ats.py
│── ai_feedback.py
│── requirements.txt
│── .env
│── README.md
```

---

## 📊 Project Workflow

```text
Upload Resume
      │
      ▼
Extract Resume Text
      │
      ▼
Paste Job Description
      │
      ▼
Calculate ATS Score
      │
      ▼
Compare Resume & Job Description
      │
      ▼
Find Matching Skills
      │
      ▼
Find Missing Skills
      │
      ▼
Generate AI Feedback
      │
      ▼
Display Results
```

---

## 📌 Output

- ATS Match Percentage
- Matching Skills
- Missing Skills
- AI Resume Feedback
- Resume Improvement Suggestions

---

## 👥 Project Team

This project was developed as a collaborative academic project.

### 👨‍💼 Team Leader

**Tushar Verma**

- B.Tech CSE (Artificial Intelligence)
- Babu Banarasi Das University, Lucknow
- GitHub: https://github.com/Tushar1752

### 👨‍💻 Team Member

**Sudhakar Agrahari**

- B.Tech CSE (Artificial Intelligence)
- Babu Banarasi Das University, Lucknow

---

## 🎯 Learning Outcomes

- Resume Parsing
- Natural Language Processing (NLP)
- ATS Score Calculation
- TF-IDF & Cosine Similarity
- AI Integration using Groq LLM
- Prompt Engineering
- Streamlit Application Development
- Python Project Structure

---

## 🚀 Future Enhancements

- Download PDF Report
- ATS Gauge Meter
- Resume Ranking
- Multiple Resume Comparison
- Job Recommendation System
- Skill Gap Analysis
- Interactive Charts
- Keyword Highlighting
- Dark Mode

---

## 📄 License

This project is developed for educational and portfolio purposes only.

---

## ⭐ Support

If you found this project helpful, please ⭐ star the repository.

### Maintained By

**Tushar Verma**

GitHub: https://github.com/Tushar1752