from fastapi import FastAPI, File, UploadFile, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sqlalchemy.orm import Session
from groq import Groq

# ✅ DB imports (CORRECT STRUCTURE)
from app.database import SessionLocal, Base, engine
from app.models import ChatHistory

# ================= CREATE TABLE =================
Base.metadata.create_all(bind=engine)

# ================= APP =================
app = FastAPI(
    title="AI Career Assistant",
    description="""
🚀 AI Career Assistant Platform

🔹 Chat with AI like ChatGPT
🔹 Get ATS Resume Score instantly
🔹 Upload & analyze resumes

👩‍💻 Built by Aishwariya A
🌐 Portfolio: https://your-portfolio-link.com
""",
    version="1.0.0",
    contact={
        "name": "Aishwariya A",
        "email": "aishwariyaalwar@gmail.com",
        "url": "https://github.com/Aishu150504"
    },
    docs_url="/docs",
    redoc_url="/redoc"
)

# ================= CORS =================
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ================= GROQ CLIENT =================
import os

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# ================= MODELS =================
class ChatRequest(BaseModel):
    prompt: str

class ChatResponse(BaseModel):
    response: str

class ATSRequest(BaseModel):
    text: str

class ATSResponse(BaseModel):
    score: int
    found_skills: list
    missing_skills: list
    recommendation: str

# ================= DB SESSION =================
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ================= ROOT =================
@app.get("/")
def home():
    return {"message": "Backend running"}

# ================= CHAT API (WITH DB SAVE) =================
@app.post("/api/chat", response_model=ChatResponse, tags=["💬 Chat AI"])
def chat(req: ChatRequest, db: Session = Depends(get_db)):

    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "system", "content": "You are a helpful career AI assistant."},
                {"role": "user", "content": req.prompt}
            ]
        )

        ai_reply = response.choices[0].message.content

    except Exception as e:
        ai_reply = f"Error: {str(e)}"

    # 💾 SAVE TO DATABASE
    chat_entry = ChatHistory(
        prompt=req.prompt,
        response=ai_reply
    )

    db.add(chat_entry)
    db.commit()

    return ChatResponse(response=ai_reply)

# ================= ATS SCORE =================
@app.post("/api/ats-score", response_model=ATSResponse, tags=["📊 ATS Analysis"])
def ats_score(req: ATSRequest):

    text = req.text.lower()

    skills_db = [
        "python", "java", "machine learning", "deep learning",
        "sql", "fastapi", "react", "nlp", "pandas", "docker"
    ]

    found = [s for s in skills_db if s in text]
    missing = list(set(skills_db) - set(found))

    score = int((len(found) / len(skills_db)) * 100)

    return ATSResponse(
        score=score,
        found_skills=found,
        missing_skills=missing,
        recommendation="Add missing skills + build AI projects + deploy on cloud"
    )

# ================= RESUME UPLOAD =================
@app.post("/api/upload-resume", tags=["📄 Resume AI"])
async def upload_resume(file: UploadFile = File(...)):

    content = await file.read()
    text = content.decode("utf-8", errors="ignore")

    return {
        "filename": file.filename,
        "word_count": len(text.split()),
        "preview": text[:300],
        "message": "Resume parsed successfully"
    }