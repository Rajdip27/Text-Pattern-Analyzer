from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from .analyzer import analyze_text

app = FastAPI(title="Text Pattern Analyzer API")

# ---------------- CORS Settings ----------------
origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,   # কে access করতে পারবে
    allow_credentials=True,
    allow_methods=["*"],     # GET, POST, PUT, DELETE
    allow_headers=["*"]      # Headers
)
# ------------------------------------------------

@app.post("/analyze")
async def analyze(
    text: str = Form(None),
    file: UploadFile = File(None)
):
    if file:
        if not file.filename.endswith(".txt"):
            return {"error": "Only .txt files are allowed"}
        text = (await file.read()).decode("utf-8")

    if not text or not text.strip():
        return {"error": "Text input is required"}

    return analyze_text(text)
