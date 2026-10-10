from fastapi import FastAPI

app = FastAPI(title: "Task Management App")

@app.get('/')
def home():
    return "Welcome to the home page"