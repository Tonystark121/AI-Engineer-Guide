Let's learn Fast API

The First question arises why fast API?
    1. fast than all other frameworks.
    2. microservices is easy to implement
    3. built on top of pydantic -> which means validation functions are on the go to implement.
    4. easy to learn and most widely used in the industry.


FIRST API Request HANDLING' - auto json format handled.

from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def home():
    return "Hello"


"Express handling" -> in expres we need to convert the format to json

const express = require('express')
app = express()

app.get('/', (req, res) => {
    res.json({
        return "Hello"
    })
})


########### Path & Query Parameters
params -> we dynamically use it in main function using {} and should present in URL as well.
Query -> don't need to be added in URL, we just define the same variable name in method and use directly. also it auto handle type error.

Compare to express params: 
    URL -> @app.get("/product/{prod_id}") while express uses : app.get("/product/:prod_id", (req, res) => {...});
    use -> get_productDetails(prod_id: int): while in expess: let id = req.params.prod_id as string so we convert it to int first for use
    params are fixed and mandatory


Compare to express Query:
    URL -> same /greet?name=Rajeev&age=25
    use -> @app.get("/greet") def greet_user(name: str, age: int): validation handled automatically
            while in express: app.get("/greet", (req, res) => { const name = req.query.name; const age = Number(req.query.age);} both as string we need to convert the data type.