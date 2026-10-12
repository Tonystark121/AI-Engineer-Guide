from fastapi import FastAPI
from src.utils.db import Base, engine
from src.task.models import TaskModal
from src.task.router import task_route
from src.user.router import user_router

app = FastAPI(title="Task Management App")

@app.on_event("startup")
def create_tables():
    Base.metadata.create_all(bind=engine)
    
app.include_router(task_route)
app.include_router(user_router)

@app.get('/')
def home():
    return "Welcome to the home page"