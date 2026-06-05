from pydantic import BaseModel

class Student(BaseModel):
    name : str = "Gaurav"

new_student = {}

student = Student(**new_student)
print(student)

 