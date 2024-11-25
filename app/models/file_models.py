from pydantic import BaseModel
from typing import Optional

class FileRequest(BaseModel):
    file: Optional[str]


class FileResponse(BaseModel):
    extracted_text: str
    summary: str

class QAResponse(BaseModel):
    question: str
    answer: str
    score: float