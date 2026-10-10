from fastapi import FastAPI, Request, HTTPException
from pydantic import BaseModel
from app.configFiles.dummyData import Products
from pathlib import Path
import pprint

class products(BaseModel):
    id: int
    name: str
    price: int
    category: str
    in_stock: bool = False

app = FastAPI()

# Get the path of the existing Python file
DATA_FILE = (
    Path(__file__).parent
    / "configFiles"
    / "dummyData.py"
)

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


@app.post("/create_product", status_code=201)
def create_Product(data:products):
    print(data)
    product_detail = data.model_dump()

    # Prevent duplicate product IDs
    if any(product["id"] == data.id for product in Products):
        raise HTTPException(
            status_code=409,
            detail="Product ID already exists"
        )
    Products.append(product_detail)
    # Convert the list into valid Python source code
    content = "Products = " + pprint.pformat(
        Products,
        sort_dicts=False
    ) + "\n"
    DATA_FILE.write_text(content, encoding="utf-8")

    print("Total products:", len(Products))
    print("Updated list:", Products)
    return {"message": "Product created Successful", "statusCode": 200, "product": product_detail, "Number_Of_Products": len(Products)}