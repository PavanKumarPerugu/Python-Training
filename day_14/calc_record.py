from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
import json, os

HISTORY_FILE = "history.json"
script_path = os.path.dirname(os.path.abspath(__file__))
history_path = os.path.join(script_path, HISTORY_FILE)

# Data model for input
class Numbers(BaseModel):
    a: float
    b: float

# Data model for history record
class OperationRecord(BaseModel):
    timestamp: str
    operation: str
    a: float
    b: float
    result: Optional[float] = None
    status : str

# Load history from file if it exists
if os.path.exists(history_path) and os.path.getsize(history_path) > 0:
    with open(history_path, "r") as f:
        history = [OperationRecord(**record) for record in json.load(f)]
else:
    history: List[OperationRecord] = []

# Helper to save history back to file
def save_history():
    with open(history_path, "w") as f:
        json.dump([record.dict() for record in history], f, indent=4)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to the Calculator API with History!"}

@app.post("/add")
def add(numbers: Numbers):
    result = numbers.a + numbers.b
    record = OperationRecord(
        timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        operation="addition",
        a=numbers.a,
        b=numbers.b,
        result=result,
        status="success"
    )
    history.append(record)
    save_history()
    return {"operation": "addition", "result": result}

@app.post("/subtract")
def subtract(numbers: Numbers):
    result = numbers.a - numbers.b
    record = OperationRecord(
        timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        operation="subtraction",
        a=numbers.a,
        b=numbers.b,
        result=result,
        status="success"
    )
    history.append(record)
    save_history()
    return {"operation": "subtraction", "result": result}

@app.post("/multiply")
def multiply(numbers: Numbers):
    result = numbers.a * numbers.b
    record = OperationRecord(
        timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        operation="multiplication",
        a=numbers.a,
        b=numbers.b,
        result=result,
        status="success"
    )
    history.append(record)
    save_history()
    return {"operation": "multiplication", "result": result}

@app.post("/divide")
def divide(numbers: Numbers):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if numbers.b == 0:
        record = OperationRecord(
            timestamp=timestamp,
            operation="division",
            a=numbers.a,
            b=numbers.b,
            result=None,
            status="failed"
        )
        history.append(record)
        save_history()
        raise HTTPException(status_code=400, detail="Cannot divide by zero")

    result = numbers.a / numbers.b
    record = OperationRecord(
        timestamp=timestamp,
        operation="division",
        a=numbers.a,
        b=numbers.b,
        result=result,
        status="success"
    )
    history.append(record)
    save_history()
    return {"operation": "division", "result": result}

@app.get("/history")
def get_history():
    return {"total_operations": len(history), "history": history}
