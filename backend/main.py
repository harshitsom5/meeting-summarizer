from fastapi import FastAPI, UploadFile, File
from pathlib import Path

app = FastAPI()

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

    return {
        "message": "Audio uploaded successfully",
        "filename": file.filename
    }