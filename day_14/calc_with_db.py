from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# ---------- Database Setup ----------
DATABASE_URL = "mysql+pymysql://root:password@localhost/calculator_db"  # change user/password
engine = create_engine(DATABASE_URL, echo=True)
Base = declarative_base()
SessionLocal = sessionmaker(bind=engine)

# ---------- SQLAlchemy Model ----------
class OperationRecord(Base):
    __tablename__ = "operation_history"

    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime, default=datetime.now)
    operation = Column(String(50))
    a = Column(Float)
    b = Column(Float)
    result = Column(Float, nullable=True)
    status = Column(String(20))

# Create table if it doesn't exist
Base.metadata.create_all(bind=engine)

# ---------- Pydantic Model ----------
class Numbers(BaseModel):
    a: float
    b: float

class OperationResponse(BaseModel):
    operation: str
    result: Optional[float]
    status: str

# ---------- FastAPI App ----------
app = FastAPI(title="Calculator API with MySQL")

# ---------- Helper to log operations ----------
def log_operation(operation: str, a: float, b: float, result: Optional[float], status: str):
    db = SessionLocal()
    record = OperationRecord(
        timestamp=datetime.now(),
        operation=operation,
        a=a,
        b=b,
        result=result,
        status=status
    )
    db.add(record)
    db.commit()
    db.close()

# ---------- Endpoints ----------
@app.get("/")
def home():
    return {"message": "Welcome to the Calculator API with MySQL!"}

@app.post("/add", response_model=OperationResponse)
def add(numbers: Numbers):
    result = numbers.a + numbers.b
    log_operation("addition", numbers.a, numbers.b, result, "success")
    return {"operation": "addition", "result": result, "status": "success"}

@app.post("/subtract", response_model=OperationResponse)
def subtract(numbers: Numbers):
    result = numbers.a - numbers.b
    log_operation("subtraction", numbers.a, numbers.b, result, "success")
    return {"operation": "subtraction", "result": result, "status": "success"}

@app.post("/multiply", response_model=OperationResponse)
def multiply(numbers: Numbers):
    result = numbers.a * numbers.b
    log_operation("multiplication", numbers.a, numbers.b, result, "success")
    return {"operation": "multiplication", "result": result, "status": "success"}

@app.post("/divide", response_model=OperationResponse)
def divide(numbers: Numbers):
    if numbers.b == 0:
        log_operation("division", numbers.a, numbers.b, None, "failed")
        raise HTTPException(status_code=400, detail="Cannot divide by zero")

    result = numbers.a / numbers.b
    log_operation("division", numbers.a, numbers.b, result, "success")
    return {"operation": "division", "result": result, "status": "success"}

@app.get("/history")
def get_history(operation: Optional[str] = Query(None, description="Filter by operation")):
    db = SessionLocal()
    query = db.query(OperationRecord)
    if operation:
        query = query.filter(OperationRecord.operation == operation.lower())
    records = query.order_by(OperationRecord.id.desc()).all()
    db.close()

    return {
        "total_operations": len(records),
        "history": [
            {
                "id": r.id,
                "timestamp": r.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
                "operation": r.operation,
                "a": r.a,
                "b": r.b,
                "result": r.result,
                "status": r.status
            }
            for r in records
        ]
    }

@app.delete("/history")
def clear_history():
    db = SessionLocal()
    db.query(OperationRecord).delete()
    db.commit()
    db.close()
    return {"message": "All history cleared successfully."}
