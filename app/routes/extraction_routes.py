from fastapi import APIRouter, Request, UploadFile, File, HTTPException
from app.services.extraction_service import (
    extract_text_from_pdf,
    extract_text_from_image,
    extract_text_from_docx,
    extract_text_from_txt,
    extract_text_from_csv
)
from app.services.summarization_service import summarize_text
from app.services.qa_service import answer_question
from app.models import FileResponse, QAResponse
from typing import List

router = APIRouter()

MAX_FILE_SIZE = 50 * 1024 * 1024

@router.post("/extract/", response_model=FileResponse)
async def extract_and_summarize(file: UploadFile = File(...)):
    if file.size > MAX_FILE_SIZE:
        raise HTTPException(status_code=413, detail="File is too large. Maximum size allowed is 50MB.")

    content = await file.read()

    if file.content_type == "application/pdf":
        extracted_text = extract_text_from_pdf(content)
    elif file.content_type.startswith("image/"):
        extracted_text = extract_text_from_image(content)
    elif file.content_type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        extracted_text = extract_text_from_docx(content)
    elif file.content_type == "text/plain":
        extracted_text = extract_text_from_txt(content)
    elif file.content_type == "text/csv":
        extracted_text = extract_text_from_csv(content)
    else:
        raise HTTPException(status_code=415, detail="Unsupported file type")

    summary = summarize_text(extracted_text)
    return FileResponse(extracted_text=extracted_text, summary=summary)

@router.post("/qa/", response_model=QAResponse)
async def question_answer(request: Request):
    body = await request.json()  # Lê os dados JSON do corpo da requisição
    context = body.get('context')
    question = body.get('question')

    if not context or not question:
        raise HTTPException(status_code=400, detail="Context and question are required.")

    result = answer_question(question, context)
    return QAResponse(question=question, answer=result["answer"], score=result["score"])
