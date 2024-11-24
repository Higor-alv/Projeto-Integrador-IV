from pydantic import BaseModel

# Modelo para receber o arquivo (caso queira adicionar metadados mais tarde)
class FileRequest(BaseModel):
    file: str  # Pode ser um campo para metadados ou outra informação

# Modelo para a resposta da extração e resumo do arquivo
class FileResponse(BaseModel):
    extracted_text: str
    summary: str
