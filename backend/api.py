from fastapi import FastAPI, UploadFile, File, Form
from analyzer_service import analyze_resume
from parser import extract_pdf_text
from models import AnalyzeRequest

app = FastAPI(
    title="AI Resume Analyzer API",
    description="AI-powered resume analyzer built with Python and FastAPI.",
    version="1.0.0",
)


@app.get("/")
def home():
    return {
        "message": "AI Resume Analyzer API is running"
    }


@app.post("/analyze")
def analyze_text(request: AnalyzeRequest):
    result = analyze_resume(
        request.resume_text,
        request.job_text
    )

    return result


@app.post("/analyze-resume")
async def analyze_uploaded_resume(
    file: UploadFile = File(...),
    job_text: str = Form(...)
):
    file_content = await file.read()

    resume_text = extract_pdf_text(file_content)

    result = analyze_resume(
        resume_text,
        job_text
    )

    return {
        "filename": file.filename,
        "analysis": result
    }
