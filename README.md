# 🚀 AI Career Assistant

An AI-powered Career Assistant platform built using FastAPI, React, Groq LLM, and Retrieval-Augmented Generation (RAG).

The platform helps users analyze resumes, evaluate ATS compatibility, identify skill gaps, generate career roadmaps, and interact with an AI-powered career mentor.

---

## 📌 Project Status

🚧 Work In Progress

This project is currently under development as part of my learning journey in Generative AI, FastAPI, and Full Stack AI Development.

Current functionality includes:
- AI Career Chat
- Resume Upload & Analysis
- ATS Resume Scoring
- Skill Gap Analysis
- Career Roadmap Generation

Additional features, deployment, and UI improvements are planned.

---

# ✨ Features

## 🤖 AI Career Chat Assistant

- Chat with an AI-powered career mentor
- Career guidance and recommendations
- Learning path suggestions

---

## 📄 Resume Analysis

- Upload resumes
- Resume parsing
- Resume insights
- Resume improvement recommendations

---

## 🎯 ATS Resume Scoring

- ATS compatibility analysis
- Resume scoring
- Improvement suggestions
- Keyword matching

---

## 📚 Skill Gap Analysis

- Compare skills against target roles
- Identify missing skills
- Personalized learning recommendations

---

## 🛣 Career Roadmap Generator

- AI-generated career roadmap
- Learning sequence recommendations
- Technology-specific guidance

---

## 🎤 Interview Preparation

- Interview question generation
- Technical interview preparation
- Behavioral interview guidance

---

# 🏗 Project Architecture

```text
AI-Research-Agent
│
├── backend
│   ├── app
│   │   ├── agents
│   │   ├── api
│   │   ├── database
│   │   ├── models
│   │   ├── services
│   │   └── data
│   │
│   └── requirements.txt
│
├── frontend
│   ├── public
│   ├── src
│   │   ├── components
│   │   ├── pages
│   │   └── api
│   │
│   └── package.json
│
├── screenshots
│
└── README.md
```

---

# ⚙️ Tech Stack

## Backend

- Python
- FastAPI
- SQLAlchemy
- Pydantic
- SQLite

## Frontend

- React
- Vite
- JavaScript
- CSS

## AI & LLM

- Groq API
- LLM Integration
- RAG Architecture

## Database

- SQLite
- ChromaDB Vector Database

---

# 📸 Screenshots

## Swagger API Documentation

![Swagger Docs](screenshots/swagger-docs.png)

---

## Home Page

![Home Page](screenshots/home-page.png)

---

## AI Career Chat

![Chat Page](screenshots/chat-page.png)

---

## ATS Resume Analysis

![ATS Page](screenshots/ats-page.png)

---

# 🚀 Getting Started

## Clone Repository

```bash
git clone https://github.com/AishwariyaAI/AI-Research-Agent.git
```

```bash
cd AI-Research-Agent
```

---

# Backend Setup

```bash
cd backend
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create `.env`

```env
GROQ_API_KEY=YOUR_GROQ_API_KEY
```

Run FastAPI:

```bash
uvicorn app.main:app --reload
```

Backend URL:

```text
http://localhost:8000
```

Swagger Docs:

```text
http://localhost:8000/docs
```

---

# Frontend Setup

```bash
cd frontend
```

Install dependencies:

```bash
npm install
```

Run frontend:

```bash
npm run dev
```

Frontend URL:

```text
http://localhost:5173
```

---

# Future Improvements

- User Authentication
- JWT Security
- PostgreSQL Integration
- Advanced RAG Pipeline
- Docker Deployment
- Cloud Deployment
- Improved UI/UX
- Resume Templates
- Real-Time Career Recommendations
- Multi-LLM Support

---

# Learning Outcomes

Through this project I gained practical experience in:

- FastAPI Development
- REST API Design
- React Frontend Development
- LLM Integration
- RAG Systems
- Vector Databases
- Git & GitHub
- Full Stack AI Development

---

# 👩‍💻 Author

### Aishwariya A

AI/ML Engineer | GenAI Developer | Full Stack AI Developer

📧 Email:
aishwariyaalwar@gmail.com

🔗 GitHub:
https://github.com/AishwariyaAI

🔗 LinkedIn:
https://www.linkedin.com

---

⭐ If you found this project interesting, feel free to star the repository.
