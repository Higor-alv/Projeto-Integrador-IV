import os
import pandas as pd
from xml.dom.minidom import Document
from docx import Document as DocxDocument
import fitz
import pytesseract
from PIL import Image
import io


def extract_text_from_pdf(pdf_content: bytes) -> str:
    pdf_document = fitz.open(stream=pdf_content, filetype="pdf")
    text = ""
    for page in pdf_document:

        text += page.get_text()

        images = page.get_images(full=True)
        for img_index, img in enumerate(images):
            xref = img[0]
            base_image = pdf_document.extract_image(xref)
            image_bytes = base_image["image"]
            image = Image.open(io.BytesIO(image_bytes))
            text += pytesseract.image_to_string(image)
    return text

def extract_text_from_image(image_content: bytes) -> str:
    image = Image.open(io.BytesIO(image_content))

    image = image.convert('L')
    image = image.point(lambda x: 0 if x < 128 else 255, '1')

    text = pytesseract.image_to_string(image)
    return text

def extract_text_from_docx(docx_content: bytes) -> str:
    try:
        docx_file = io.BytesIO(docx_content)
        doc = DocxDocument(docx_file)

        text = []
        for para in doc.paragraphs:
            text.append(para.text)

        return "\n".join(text)
    except Exception as e:
        raise Exception(f"Erro ao processar arquivo .docx: {str(e)}")


def extract_text_from_txt(txt_content: bytes) -> str:
    try:
        return txt_content.decode('utf-8')
    except Exception as e:
        raise Exception(f"Erro ao processar arquivo .txt: {str(e)}")




def extract_text_from_csv(csv_content: bytes) -> str:
    try:
        df = pd.read_csv(io.BytesIO(csv_content))
        return df.to_string(index=False)
    except Exception as e:
        raise Exception(f"Erro ao processar arquivo .csv: {str(e)}")
