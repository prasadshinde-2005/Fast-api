from fastapi import FastAPI ,  HTTPException , Path
import json
from pathlib import Path

app = FastAPI()

@app.get("/")
def greet():
    return{"Hello gays this is me sp , you are with , today i will tell about me and myself ,Please leasean carefully"}


@app.get("/hello")
def hello():
    return{"This is Hello page"}

# load the data from json file 
def load_data():
    file_path = Path(__file__).parent / "student.json"

    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)

 
@app.get("/student")
def student():
    return load_data()   


# student_id --> path parameter 
@app.get("/students/{student_id}")
def get_id(student_id: str = Path(...,description ="The Id of the student" ,
            examples =["STU002"])):
    data = load_data()

    if student_id not in data:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return data[student_id]