from fastapi import FastAPI, UploadFile, File
from fastapi.staticfiles import StaticFiles
from app.routes.item_routes import router as item_router
from app.routes.user_routes import router as user_router
from app.routes.extraction_routes import router as extraction_router
from app.services import extract_text_from_pdf, extract_text_from_image
from app.services import summarize_text
from fastapi.middleware.cors import CORSMiddleware

from app.services.extraction_service import extract_text_from_docx


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="app/static"), name="static")

app.include_router(item_router)
app.include_router(user_router)
app.include_router(extraction_router)


@app.post("/extract_pdf/")
async def extract_pdf(file: UploadFile = File(...)):
    try:
        content = await file.read()
        extracted_text = extract_text_from_pdf(content)
        summary = summarize_text(extracted_text)
        return {"extracted_text": extracted_text, "summary": summary}
    except Exception as e:
        return {"error": str(e)}

@app.post("/extract_image/")
async def extract_image(file: UploadFile = File(...)):
    try:
        content = await file.read()
        extracted_text = extract_text_from_image(content)
        summary = summarize_text(extracted_text)
        return {"extracted_text": extracted_text, "summary": summary}
    except Exception as e:
        return {"error": str(e)}

@app.post("/extract_docx/")
async def extract_docx(file: UploadFile = File(...)):
    try:
        content = await file.read()  # Ler o conteúdo do arquivo enviado
        extracted_text = extract_text_from_docx(content)  # Extrair texto
        summary = summarize_text(extracted_text)  # Resumir texto
        return {"extracted_text": extracted_text, "summary": summary}
    except Exception as e:
        return {"error": str(e)}
