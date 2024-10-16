import fitz  # PyMuPDF
import pytesseract
from PIL import Image
import io

def extract_text_from_pdf(pdf_content: bytes) -> str:
    pdf_document = fitz.open(stream=pdf_content, filetype="pdf")
    text = ""
    for page in pdf_document:
        text += page.get_text()
    return text

def extract_text_from_image(image_content: bytes) -> str:
    image = Image.open(io.BytesIO(image_content))
    text = pytesseract.image_to_string(image)
    return text
