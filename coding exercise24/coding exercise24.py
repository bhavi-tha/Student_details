student_data=[
    {
      "Name":"Ram",
      "roll_no":10,
      "age":20,
      "branch":"CSE",
    },
    {
        "Name":"HP",
        "roll_no":20,
        "age":22,
        "branch":"CSM",
    }
]
def add_new_student(name,roll_no,age,branch):
    new_student = {}
    new_student["name"] = name
    new_student["roll_no"] = roll_no
    new_student["age"] = age
    new_student["branch"] = branch
    student_data.append(new_student)
add_new_student("mohan",11,10,"ECE")
print(student_data)
