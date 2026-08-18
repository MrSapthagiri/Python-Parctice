print("Hello, World!")
name = "Santhosh"
print(name)

name = input("Enter your name: ")
print(name)

name = input("Enter your name: ")
print("Hello", name)

student_ID = 100087
student_Name= "Ashwin"
age = 21
department = "Computer science"
cgpa = 89.05
passed_Status = True

print(student_ID)
print(student_Name)
print(age)
print(department)
print(cgpa)
print(passed_Status)

subject = ["physics","chemistry","data science"]
print(subject)

subject.append("computer")
print(subject)

subject.remove("data science")
print(subject)

x = len(subject)
print(x)

semesterSubject = ("Datascience","cybersecurity","algorithm")
print(semesterSubject)

student_Information = {
    "id" : 100087,
    "name" : "Ashwin",
    "age" : 23,
    "department" : "computerscience",
    "cgpa" : 99.05
}
#print age
print(student_Information)  # I don't know how to call induvidual data

stundent_Skill = {"dance","karate","drawing","fencing"}
stundent_Skill.remove("drawing")

print(stundent_Skill)

semester_Subject = frozenset({"Datascience","cybersecurity","algorithm"})
print(semester_Subject)

newrange = 14
roll_Number = range(15)
for n in roll_Number:
    print(n)

is_eligible = True
if is_eligible:
    print("The student  $ {newrange}is eligible for placement.")


# Task 9 - Student Signature

signature = b"Shaja"

print("Student Signature (Binary):", signature)


# Task 10 - Student Photo
photo = bytearray(b"StudentPhoto")

print("Editable Photo Data:", photo)


placement_Company = None
print("Placement Company:", placement_Company)


student_ID = float(100087) 
number = int("-345")
age = str(32)
department = list("Computer science")

name = "shajahan"
print(type(name))

name = "Eswaran"
print(id(name))