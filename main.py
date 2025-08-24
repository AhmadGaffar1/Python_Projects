########################################################################################################################
# cd PyCharmProjects/FastAPI_01

from fastapi import FastAPI,Body
from uuid import UUID, uuid4

app = FastAPI()

########################################################################################################################

class Student():

    id: UUID
    name: str
    age: int
    grade: float

    def __init__(self,name: str,age: int,grade: float):
        self.id=uuid4()
        self.name=name
        self.age=age
        self.grade=grade

    def return_json(self):
        return {
            "id": str(self.id),
            "name": self.name,
            "age": self.age,
            "grade": self.grade,
        }

students = [
    Student("Ahmad", 28, 5),
    Student("Mohamed", 30, 3),
    Student("Mostafa", 29, 4.5),
    Student("Karim", 32, 5)
]

########################################################################################################################

# website root
@app.get("/", description="this is the root page for the website")
def root():
    return {"message": "Hello Everyone"}



# end-point for display all students
@app.get("/display_all_students/", description="this page display all data for each student enrolled in the university")
def display_all_students():
    return students
    # return [ st.return_json() for st in students ]



# end-point for display all students
@app.get("/display_all_students_IDs/", description="this page display ID for all students enrolled in the university")
def display_all_students_IDs():
    IDs=[]
    for st in students:
        IDs.append(st.id)
    return IDs



# end-point for searching for a particular student by ( ID )
@app.get("/display_student_by_id/{id}/", description="this page for searching for any student by ID")
def display_student_by_id(id: UUID):
    for st in students:
        if (st.id == id):
            return st
            # return st.return_json()
    return {"This Student ID not exist in database !"}



# end-point for searching for a particular student by ID
@app.get("/filtering_students_by_gardes/", description="this page for searching for any student by ID")
def filtering_students_by_grades(Min_Grade: float,Max_Grade: float):
    list = []
    for i in range(len(students)):
        if (students[i].grade >= Min_Grade and students[i].grade <= Max_Grade):
            list.append(students[i])
    if (len(list) == 0):
        return {"There are no students within this grade range"}
    else:
        return list
        # return [ st.return_json() for st in list ]



# end-point for inserting new student in database
@app.post("/inserting_new_student/", description="this page for adding a new student in database\nNOTE: when excuted, can get it from the get endpoints")
def inserting_new_student(name: str = Body(...), age: int = Body(...), grade: float = Body(...) ):
    new_student= Student(name,age,grade)
    students.append(new_student)
    return {"Recieved Student" : new_student}
    # return {"Recieved Student" : new_student.return_json()}



# end-point for update a particular student
@app.put("/updating_student/{id}", description="this page search for any student by ID, and then display his data for ability to modifying it")
def updating_student(id: UUID, name: str = Body(...), age: int = Body(...), grade: float = Body(...) ):
    for i in range(len(students)):
        if students[i].id == id:
            students[i].name=name
            students[i].age=age
            students[i].grade=grade
            return {"Updated Student" : students[i]}
            # return {"Updated Student" : students[i].return_json()}



# end-point for delete a particular student
@app.delete("/deleting_student_by_id/{id}/", description="this page for searching for any student by ID")
def deleting_student_by_id(id: UUID):
    for i in range(len(students)):
        if students[i].id == id:
            return {"Deleted Student" : students.pop(i)}



########################################################################################################################