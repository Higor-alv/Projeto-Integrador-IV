from pydantic import BaseModel

class SummaryResponse(BaseModel):
    extracted_text: str
    summary: str
