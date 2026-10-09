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