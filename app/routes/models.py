from pydantic import BaseModel
from typing import Optional

# Definindo o modelo Item com Pydantic
class Item(BaseModel):
    id: Optional[int] = None  # ID pode ser opcional para inserções
    name: str
    description: Optional[str] = None

# Exemplo de outro modelo, como User
class User(BaseModel):
    id: Optional[int] = None
    username: str
    email: str
