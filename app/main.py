from fastapi import FastAPI, UploadFile, File
from services.extraction_service import extract_text_from_pdf, extract_text_from_image
from services.summarization_service import summarize_text

app = FastAPI()

@app.post("/extract_pdf/")
async def extract_pdf(file: UploadFile = File(...)):
    content = await file.read()
    extracted_text = extract_text_from_pdf(content)
    summary = summarize_text(extracted_text)
    return {"extracted_text": extracted_text, "summary": summary}

@app.post("/extract_image/")
async def extract_image(file: UploadFile = File(...)):
    content = await file.read()
    extracted_text = extract_text_from_image(content)
    summary = summarize_text(extracted_text)
    return {"extracted_text": extracted_text, "summary": summary}