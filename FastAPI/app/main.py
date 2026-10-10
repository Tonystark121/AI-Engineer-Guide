from fastapi import FastAPI, Request
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

# now query params are not fixed it can be of any number so we how to handle that
@app.get("/greet")
def greet_user(request:Request):
    query_params = dict(request.query_params)
    print(request, query_params)
    try:
        age = int(query_params.get("age"))
    except ValueError:
        return {"error": "There is error in query string, Age should be an integer"}
    return f"Hello {query_params.get("name")} How are you? is your age {query_params.get("age")}"