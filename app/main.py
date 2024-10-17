from fastapi import FastAPI, UploadFile, File
from app.routes.item_routes import router as item_router
from app.routes.user_routes import router as user_router  # Certifique-se de importar corretamente
from app.routes.extraction_routes import router as extraction_router
from app.services import extract_text_from_pdf, extract_text_from_image
from app.services import summarize_text

app = FastAPI()

# Incluindo os roteadores
app.include_router(item_router)
app.include_router(user_router)
app.include_router(extraction_router)



# @app.post("/extract_pdf/")
# async def extract_pdf(file: UploadFile = File(...)):
#     content = await file.read()
#     extracted_text = extract_text_from_pdf(content)
#     summary = summarize_text(extracted_text)
#     return {"extracted_text": extracted_text, "summary": summary}

@app.post("/extract_image/")
async def extract_image(file: UploadFile = File(...)):
    content = await file.read()
    extracted_text = extract_text_from_image(content)
    summary = summarize_text(extracted_text)
    return {"extracted_text": extracted_text, "summary": summary}
