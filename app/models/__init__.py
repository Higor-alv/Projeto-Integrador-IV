from pydantic import BaseModel

class FileRequest(BaseModel):
    file: str

class FileResponse(BaseModel):
    extracted_text: str
    summary: str

class QAResponse(BaseModel):
    question: str
    answer: str
    score: float