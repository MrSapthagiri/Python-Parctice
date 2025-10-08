# 01_syntax.py
# -----------------------------
# Print
# -----------------------------
print("Hello, World!")
print(5 + 3)

# -----------------------------
# Comments
# -----------------------------
# Single-line comment
"""
Multi-line
comment
"""

# -----------------------------
# Variables & Data Types
# -----------------------------
x = 10              # int
y = 3.14            # float
name = "Alice"      # string
is_active = True    # boolean
nums = [1, 2, 3]    # list
tup = (1, 2, 3)     # tuple
person = {"name": "Bob", "age": 25}  # dictionary
s = {1, 2, 3}       # set

print(type(x), type(y), type(name), type(is_active))

# -----------------------------
# Input
# -----------------------------
# user_input = input("Enter something: ")
# print("You entered:", user_input)

# -----------------------------
# If-Else
# -----------------------------
num = 7
if num > 0:
    print("Positive")
elif num == 0:
    print("Zero")
else:
    print("Negative")

# -----------------------------
# Loops
# -----------------------------
# For loop
for i in range(5):
    print("For:", i)

# While loop
count = 0
while count < 3:
    print("While:", count)
    count += 1

# -----------------------------
# Functions
# -----------------------------
def add(a, b):
    return a + b

print("Sum:", add(5, 3))

# -----------------------------
# String Operations
# -----------------------------
text = "Python"
print(text.upper())
print(text.lower())
print(text[0])       # first char
print(text[-1])      # last char
print(len(text))

# -----------------------------
# List Operations
# -----------------------------
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
fruits.remove("banana")
print(fruits)
print(fruits[0])    # first item

# -----------------------------
# Dictionary Operations
# -----------------------------
person = {"name": "Alice", "age": 30}
print(person["name"])
person["age"] = 31
print(person)

# -----------------------------
# Set Operations
# -----------------------------
A = {1, 2, 3}
B = {3, 4, 5}
print(A | B)   # Union
print(A & B)   # Intersection
print(A - B)   # Difference

# -----------------------------
# Tuple
# -----------------------------
point = (2, 3)
print(point[0], point[1])

# -----------------------------
# Class & Object (OOP)
# -----------------------------
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        return f"Hello, my name is {self.name}"

p1 = Person("John", 25)
print(p1.greet())

# -----------------------------
# Exception Handling
# -----------------------------
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Division by zero not allowed")
finally:
    print("Done")

# -----------------------------
# Import & Math
# -----------------------------
import math
print(math.sqrt(16))
print(math.pi)

# -----------------------------
# File Handling
# -----------------------------
with open("sample.txt", "w") as f:
    f.write("Hello File!")

with open("sample.txt", "r") as f:
    print(f.read())

# This covers:

    # Print, comments, variables, input

    # If-Else, loops, functions

    # Strings, lists, dicts, sets, tuples

    # Classes & objects

    # Exception handling

    # Math & file handling
    
# Python syntax with built-in functions and features — not just basics.!

# -----------------------------
# Print & Formatting
# -----------------------------
print("Hello", "World", sep="-")   # Hello-World
print("Name: {}, Age: {}".format("Alice", 25))
print(f"Square of 5 = {5**2}")     # f-string

# -----------------------------
# Type Casting
# -----------------------------
x = int("10")     # str → int
y = float("3.14") # str → float
z = str(123)      # int → str
print(type(x), type(y), type(z))

# -----------------------------
# Math Functions
# -----------------------------
print(abs(-7))       # absolute value
print(round(3.567, 2))  # round to 2 decimals
print(pow(2, 3))     # 2^3
print(min(1, 5, 3))  # minimum
print(max(1, 5, 3))  # maximum
print(sum([1, 2, 3])) # sum of list

# -----------------------------
# String Functions
# -----------------------------
s = "  Python Basics  "
print(s.strip())      # remove spaces
print(s.lower())      # lowercase
print(s.upper())      # uppercase
print(s.replace("Python", "Java"))
print("apple,banana".split(","))  # split into list
print("-".join(["one", "two", "three"]))  # join list into string

# -----------------------------
# List Functions
# -----------------------------
nums = [5, 2, 9, 1]
print(len(nums))       # length
print(sorted(nums))    # sort
nums.sort(reverse=True)
print(nums)
print(max(nums), min(nums))

# List comprehension
squares = [i**2 for i in range(5)]
print(squares)

# -----------------------------
# Dictionary Functions
# -----------------------------
person = {"name": "Alice", "age": 25}
print(person.keys())   # dict keys
print(person.values()) # dict values
print(person.items())  # key-value pairs
print(person.get("name", "Not found"))  # safe get

# -----------------------------
# Set Functions
# -----------------------------
A = {1, 2, 3}
B = {3, 4, 5}
print(A.union(B))
print(A.intersection(B))
print(A.difference(B))

# -----------------------------
# Built-in Functions
# -----------------------------
print(type(123))       # type
print(isinstance(3.14, float))  # check type
print(all([True, True, False])) # all true?
print(any([True, False, False]))# any true?

# -----------------------------
# Lambda Function
# -----------------------------
square = lambda x: x*x
print(square(5))

nums = [1, 2, 3, 4, 5]
doubled = list(map(lambda n: n*2, nums))
evens = list(filter(lambda n: n%2==0, nums))
print(doubled)
print(evens)

# -----------------------------
# Enumerate & Zip
# -----------------------------
fruits = ["apple", "banana", "cherry"]
for idx, val in enumerate(fruits):
    print(idx, val)

colors = ["red", "yellow", "pink"]
for f, c in zip(fruits, colors):
    print(f, "->", c)

# -----------------------------
# Range & Slicing
# -----------------------------
print(list(range(1, 6)))
print(fruits[0:2])   # slice
print(fruits[-1])    # last item

# -----------------------------
# Try-Except (Error Handling)
# -----------------------------
try:
    val = int("abc")
except ValueError:
    print("Invalid conversion")

# -----------------------------
# File Handling
# -----------------------------
with open("demo.txt", "w") as f:
    f.write("Python is great!")

with open("demo.txt", "r") as f:
    print(f.read())
# This file extends the basics with built-in functions and features.

#Now your syntax includes:
# ✔️ Print & formatting
# ✔️ Type casting
# ✔️ Math functions (abs, round, pow, sum, min, max)
# ✔️ String functions (strip, split, join, replace)
# ✔️ List, dict, set functions
# ✔️ Built-ins (all, any, isinstance)
# ✔️ Lambda, map, filter
# ✔️ Enumerate & zip
# ✔️ File handling