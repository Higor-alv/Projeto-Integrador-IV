from fastapi import FastAPI
from .routes import user_routes, item_routes

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the API!"}

app.include_router(user_routes, prefix="/users")
app.include_router(item_routes, prefix="/items")
