from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Numbers(BaseModel):
    a: float
    b: float

@app.get("/")
def home():
    return {"message": "Welcome to the Calculator API"}

@app.post("/add")
def add(numbers: Numbers):
    return {"result": numbers.a + numbers.b}

@app.post("/subtract")
def subtract(numbers: Numbers):
    return {"result": numbers.a - numbers.b}

@app.post("/multiply")
def multiply(numbers: Numbers):
    return {"result": numbers.a * numbers.b}

@app.post("/divide")
def divide(numbers: Numbers):
    if numbers.b == 0:
        return {"error": "Cannot divide by zero"}
    return {"result": numbers.a / numbers.b}
