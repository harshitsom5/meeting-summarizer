from backend.summarizer import summarize_transcript
from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pathlib import Path
from backend.transcriber import transcribe_audio

app = FastAPI()

app.mount(
    "/frontend",
    StaticFiles(directory="frontend", html=True),
    name="frontend"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)


@app.get("/")
def home():
    return {"message": "Meeting Summarizer API is running"}


@app.post("/upload")
async def upload_audio(file: UploadFile = File(...)):
    file_path = UPLOAD_DIR / file.filename

    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    transcript = transcribe_audio(str(file_path))
    summary = summarize_transcript(transcript)

    return {
        "message": "Audio uploaded, transcribed and summarized successfully",
        "filename": file.filename,
        "transcript": transcript,
        "summary": summary
    }