from fastapi import APIRouter, UploadFile, File
from app.services.extraction_service import extract_text_from_pdf, extract_text_from_image
from app.services.summarization_service import summarize_text

router = APIRouter()

@router.post("/extract/")
async def extract_and_summarize(file: UploadFile = File(...)):
    content = await file.read()

    if file.content_type == "application/pdf":
        extracted_text = extract_text_from_pdf(content)
    elif file.content_type.startswith("image/"):
        extracted_text = extract_text_from_image(content)
    else:
        return {"error": "Unsupported file type"}

    summary = summarize_text(extracted_text)
    return {"extracted_text": extracted_text, "summary": summary}
