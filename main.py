from fastapi import FastAPI

app = FastAPI()

students = {}

@app.get("/")
def read_root():
    return {"message": "Welcome to the University API!"}

@app.post("/students/{student_id}")
def create_student(student_id: int, name: str):
    students[student_id] = name
    return {"student_id": student_id, "name": name}
 
@app.get("/students/{student_id}")
def read_student(student_id: int):
    if student_id not in students:
        return {"error": "Student not found"}
    return {"student_id": student_id, "name": students[student_id]}