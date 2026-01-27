from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to the Calculator API!"}


@app.get("/add")
def add(a: float, b: float):
    return {"operation": "addition", "a": a, "b": b, "result": a + b}


@app.get("/subtract")
def subtract(a: float, b: float):
    return {"operation": "subtraction", "a": a, "b": b, "result": a - b}


@app.get("/multiply")
def multiply(a: float, b: float):
    return {"operation": "multiplication", "a": a, "b": b, "result": a * b}


@app.get("/divide")
def divide(a: float, b: float):
    if b == 0:
        return {"error": "Cannot divide by zero"}
    return {"operation": "division", "a": a, "b": b, "result": a / b}
