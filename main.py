from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

students = {}

class StudentCreate(BaseModel):
    name: str

@app.get("/")
def read_root():
    return {"message": "Welcome to the University API!"}

@app.post("/students/{student_id}")
def create_student(student_id: int, student: StudentCreate):
    students[student_id] = student.name
    return {"student_id": student_id, "name": student.name}

@app.get("/students/{student_id}")
def read_student(student_id: int):
    if student_id not in students:
        raise HTTPException(status_code=404, detail="Student not found")
    return {"student_id": student_id, "name": students[student_id]}