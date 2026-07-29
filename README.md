# 📄 AI Resume Analyzer

A modern AI-powered Resume Analyzer built using **Python**, **Natural Language Processing (NLP)** and **Machine Learning**.

It helps job seekers analyse their resumes against a Job Description by extracting skills, calculating resume similarity, estimating an ATS score, generating a PDF report, and storing previous analyses.

---

## 🚀 Features

- 📂 Upload Resume (PDF & DOCX)
- 📝 Resume Text Extraction
- 🧹 NLP Text Preprocessing
- 🛠 Skill Extraction
- 📊 Resume Match Score
- 🎯 ATS Score Calculation
- ✅ Matching Skills
- ❌ Missing Skills
- 💡 Resume Improvement Suggestions
- 📈 Dashboard Charts
- 📄 Download PDF Report
- 🗄 Analysis History using SQLite Database

---

## 🛠 Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| Streamlit | Web Application |
| spaCy | NLP |
| Scikit-learn | Resume Matching |
| Pandas | Data Processing |
| Matplotlib | Charts |
| SQLite | Database |
| ReportLab | PDF Report |

---

## 📂 Project Structure

```text
AI-Resume-Analyzer/
│
├── app.py
├── README.md
├── requirements.txt
├── .gitignore
│
├── data/
│   └── skills.csv
│
├── screenshots/
│   ├── home.png
│   ├── analysis.png
│   ├── dashboard.png
│   └── history.png
│
├── utils/
│   ├── parser.py
│   ├── preprocess.py
│   ├── skills.py
│   ├── similarity.py
│   ├── ats.py
│   ├── charts.py
│   ├── database.py
│   └── pdf_report.py
```

---

## 📸 Screenshots

### 🏠 Home Page

![Home](screenshots/home.png)

### 📊 Resume Analysis

![Analysis](screenshots/analysis.png)

### 📈 Dashboard

![Dashboard](screenshots/dashboard.png)

### 🗄 Analysis History

![History](screenshots/history.png)

---

# ⚙️ Installation

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/Snehal-126/AI-Resume-Analyzer.git
```

Move into the project folder:

```bash
cd AI-Resume-Analyzer
```

---

## 2️⃣ Create a Virtual Environment

### Windows

```bash
python -m venv venv
```

Activate the environment:

```bash
venv\Scripts\activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Download the spaCy Model

```bash
python -m spacy download en_core_web_sm
```

---

## 5️⃣ Run the Application

```bash
streamlit run app.py
```

The application will open in your browser at:

```
http://localhost:8501
```

---

# 🧠 How It Works

### Step 1

Upload a Resume in **PDF** or **DOCX** format.

↓

### Step 2

The application extracts the resume text.

↓

### Step 3

The text is cleaned using NLP preprocessing:

- Remove URLs
- Remove Email IDs
- Remove Phone Numbers
- Remove Stopwords
- Lemmatization

↓

### Step 4

Skills are extracted from the processed text.

↓

### Step 5

The Job Description is processed using the same NLP pipeline.

↓

### Step 6

Machine Learning (TF-IDF + Cosine Similarity) calculates the Resume Match Score.

↓

### Step 7

An ATS Score is estimated.

↓

### Step 8

The application displays:

- Resume Match Score
- ATS Score
- Matching Skills
- Missing Skills
- Resume Suggestions
- Dashboard Charts

↓

### Step 9

Generate and download a PDF report.

↓

### Step 10

Save analysis history using SQLite.

---

# 📈 Future Improvements

- AI-powered resume suggestions using Large Language Models
- Support for multiple languages
- Dark Mode
- Resume ranking for multiple applicants
- Company-specific ATS optimisation
- Keyword highlighting inside resumes
- Resume score trends over time
- User authentication

---

# 👩‍💻 Author

**Snehal Patil**

Computer Engineering Student

GitHub:

https://github.com/Snehal-126

---

# 🙏 Acknowledgements

This project was developed for learning and portfolio purposes using:

- Python
- Streamlit
- spaCy
- Scikit-learn
- ReportLab
- SQLite
- Matplotlib

---

# ⭐ If you like this project

Give this repository a ⭐ on GitHub.

It helps others discover the project and motivates future improvements.

---
