from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# This will act like our database
students = []

# This defines how student data should look
class Student(BaseModel):
    name: str
    roll_no: int
    marks: int

@app.get("/")
def home():
    return {"message": "Student Result API is running"}

@app.post("/add-student")
def add_student(student: Student):

    if student.marks >= 90:
        grade = "A"
    elif student.marks >= 75:
        grade = "B"
    elif student.marks >= 60:
        grade = "C"
    else:
        grade = "Fail"

    record = {
        "name": student.name,
        "roll_no": student.roll_no,
        "marks": student.marks,
        "grade": grade
    }

    students.append(record)

    return {"message": "Student added", "data": record}
@app.get("/students")
def get_students():
    return students
@app.get("/student/{roll_no}")
def get_student(roll_no: int):
    for s in students:
        if s["roll_no"] == roll_no:
            return s
    return {"error": "Student not found"}
