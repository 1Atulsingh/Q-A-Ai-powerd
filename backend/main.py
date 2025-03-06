from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
from quiz_generator import generate_mcqs
from PyPDF2 import PdfReader
import os

app = FastAPI()

class QuizRequest(BaseModel):
    text: str

@app.get("/")
def home():
    return {"message": "AI-Powered Quiz Generator API"}

@app.post("/generate_quiz/")
async def generate_quiz(request: QuizRequest):
    mcqs = generate_mcqs(request.text)
    return {"mcqs": mcqs}

@app.post("/upload_pdf/")
async def upload_pdf(file: UploadFile = File(...)):
    contents = await file.read()
    file_path = f"temp_{file.filename}"

    with open(file_path, "wb") as f:
        f.write(contents)

    reader = PdfReader(file_path)
    text = "\n".join([page.extract_text() for page in reader.pages if page.extract_text()])

    os.remove(file_path)  # Clean up
    return {"text": text}
