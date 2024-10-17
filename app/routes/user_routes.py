from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, EmailStr  # Importar Pydantic
from typing import Optional

router = APIRouter()

users = []
user_id_counter = 1

class User(BaseModel):
    id: int
    name: str
    email: EmailStr
    is_active: bool = True

class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    is_active: Optional[bool] = None

@router.get("/users")
def get_users():
    return users

@router.post("/users")
def create_user(user: User):
    global user_id_counter
    user_data = user.dict()
    user_data['id'] = user_id_counter
    users.append(user_data)
    user_id_counter += 1
    return user_data

@router.get("/users/{user_id}")
def get_user(user_id: int):
    for user in users:
        if user['id'] == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")

@router.put("/users/{user_id}")
def update_user(user_id: int, user_update: UserUpdate):
    for i, user in enumerate(users):
        if user['id'] == user_id:
            user_data = users[i]
            update_data = user_update.dict(exclude_unset=True)
            user_data.update(update_data)
            return user_data
    raise HTTPException(status_code=404, detail="User not found")

@router.delete("/users/{user_id}")
def delete_user(user_id: int):
    for i, user in enumerate(users):
        if user['id'] == user_id:
            del users[i]
            return {"message": "User deleted"}
    raise HTTPException(status_code=404, detail="User not found")
