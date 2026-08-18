# Python Data Types - Student Task

# Task 1 - Print Hello World
print("Hello, World!")

# Task 2 - Store and print a name
name = "Santhosh"
print(name)

# Task 3 - Get name from user
name = input("Enter your name: ")
print(name)

# Task 4 - Get name and print greeting
name = input("Enter your name: ")
print("Hello", name)

# Task 5 - Student Information
student_ID = 100087
student_Name = "Ashwin"
age = 21
department = "Computer Science"
cgpa = 89.05
passed_Status = True

print(student_ID)
print(student_Name)
print(age)
print(department)
print(cgpa)
print(passed_Status)

# Task 6 - List
subject = ["physics", "chemistry", "data science"]
print(subject)

subject.append("computer")
print(subject)

subject.remove("data science")
print(subject)

x = len(subject)
print(x)

# Task 7 - Tuple
semesterSubject = ("Datascience", "cybersecurity", "algorithm")
print(semesterSubject)

# Task 8 - Dictionary
student_Information = {
    "id": 100087,
    "name": "Ashwin",
    "age": 23,
    "department": "Computer Science",
    "cgpa": 99.05
}

print(student_Information)

# Access individual dictionary values
print(student_Information["id"])
print(student_Information["name"])
print(student_Information["age"])
print(student_Information["department"])
print(student_Information["cgpa"])

# Task 9 - Set
student_Skill = {"dance", "karate", "drawing", "fencing"}
student_Skill.remove("drawing")

print(student_Skill)

# Task 10 - Frozenset
semester_Subject = frozenset({
    "Datascience",
    "cybersecurity",
    "algorithm"
})
print(semester_Subject)

# Task 11 - Range
# range(1, 16) gives roll numbers from 1 to 15
roll_Number = range(1, 16)

for n in roll_Number:
    print(n)

# Task 12 - Boolean
is_eligible = True

if is_eligible:
    print("The student is eligible for placement.")

# Task 13 - Student Signature
signature = b"Shaja"
print("Student Signature (Binary):", signature)

# Task 14 - Student Photo
photo = bytearray(b"StudentPhoto")
print("Editable Photo Data:", photo)

# Task 15 - None
placement_Company = None
print("Placement Company:", placement_Company)

# Task 16 - Type Conversion
student_ID = float(100087)
number = int("-345")
age = str(32)

# Keep department as a single string/list value instead of
# converting every character into a separate list item.
department = ["Computer Science"]

print(student_ID)
print(number)
print(age)
print(department)

# Task 17 - type()
name = "shajahan"
print(type(name))

# Task 18 - id()
name = "Eswaran"
print(id(name))
