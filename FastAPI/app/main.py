from fastapi import FastAPI
from app.configFiles.dummyData import Products

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to the Home page"}

@app.get("/contact")
def contact():
    return {"message": "Welcome to the Contact page"}

@app.get("/products")
def get_products():
    return Products

# we have two things first Parameters & Query String
@app.get("/product/{prod_id}")
def get_productDetails(prod_id : int):
    for i in range(len(Products)):
        if(i==prod_id):
            return Products[i]

    return {
        "error": "related products not found"
    }
@app.get("/greet")
def greet_user(name:str, age:int):
    return f"Hello {name}, How are you? Are your age is {age}?"