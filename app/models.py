#

from typing import Optional
from pydantic import BaseModel

class Item(BaseModel):
    id: int = None  
    name: str
    description: str

class User(BaseModel):
    id: Optional[int] = None
    username: str
    email: str
