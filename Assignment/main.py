# First step is start a server

from fastapi import FastAPI
from src.router import router

app = FastAPI(title = "GPT Task Assignment")

app.include_router(router)

@app.get('/')
def homePage():
    return {"message": "Welcome to homepage"}
