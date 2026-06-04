from fastapi import FastAPI, UploadFile, File
from pypdf import PdfReader
import io

app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "Resume Analyzer API is running"
    }


@app.post("/upload-resume")
async def upload_resume(file: UploadFile = File(...)):
    file_bytes = await file.read()

    pdf_file = io.BytesIO(file_bytes)

    reader = PdfReader(pdf_file)

    resume_text = ""

    for page in reader.pages:
        text = page.extract_text()

        if text:
            resume_text = resume_text + text + "\n"

    return {
        "filename": file.filename,
        "text": resume_text
    }
