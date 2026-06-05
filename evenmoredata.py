import json 
student = {
    "name" :"Advaya",
    "marks" : "100"
}
with open("student.json","w") as file:
    json.dump(student, file)