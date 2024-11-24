from fastapi import APIRouter, UploadFile, File
from app.services.extraction_service import extract_text_from_pdf, extract_text_from_image, extract_text_from_docx, extract_text_from_txt, extract_text_from_csv
from app.services.summarization_service import summarize_text
from app.models import FileResponse
from typing import List

router = APIRouter()


MAX_FILE_SIZE = 50 * 1024 * 1024

@router.post("/extract/", response_model=FileResponse)
async def extract_and_summarize(file: UploadFile = File(...)):
    if file.size > MAX_FILE_SIZE:
        return {"error": "File is too large. Maximum size allowed is 50MB."}

    content = await file.read()

    # Extrai o texto com base no tipo de arquivo
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
        return {"error": "Unsupported file type"}

    # Processa grandes textos em partes menores para resumir
    summary = summarize_text(extracted_text)

    return FileResponse(extracted_text=extracted_text, summary=summary)
