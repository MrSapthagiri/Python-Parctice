# Python Variables - Complete Guide

## Table of Contents

1.  What is a Variable?
2.  Why Use Variables?
3.  Variable Syntax
4.  How Python Stores Variables
5.  Dynamic Typing
6.  Variable Assignment
7.  Multiple Assignment
8.  Variable Reassignment
9.  Checking Data Types
10. Naming Rules
11. Naming Conventions (PEP 8)
12. Reserved Keywords
13. Case Sensitivity
14. Variable Scope
15. Memory Address (`id()`)
16. Delete Variables
17. Type Casting
18. Common Data Types
19. Mutable vs Immutable
20. Real-Time Examples
21. Common Mistakes


------------------------------------------------------------------------

# 1. What is a Variable?

A **variable** is a named reference to a value stored in memory. It
allows you to store, access, and modify data during program execution.

Example:

``` python
name = "Santhosh"
age = 25
salary = 50000.50
```

------------------------------------------------------------------------

# 2. Why Use Variables?

Variables make programs:

-   Easy to read
-   Easy to maintain
-   Reusable
-   Easy to modify

``` python
url = "https://example.com"
username = "admin"
password = "Admin123"
```

------------------------------------------------------------------------

# 3. Variable Syntax

``` python
variable_name = value
```

Examples:

``` python
name = "John"
age = 25
price = 99.99
```

------------------------------------------------------------------------

# 4. How Python Stores Variables

``` python
name = "John"
```

Python:

1.  Creates the object `"John"` in memory.
2.  Creates the variable `name`.
3.  Makes `name` refer to that object.

------------------------------------------------------------------------

# 5. Dynamic Typing

Python determines the type automatically.

``` python
x = 10
print(type(x))

x = "Hello"
print(type(x))
```

Output:

    <class 'int'>
    <class 'str'>

------------------------------------------------------------------------

# 6. Variable Assignment

``` python
city = "Chennai"
marks = 95
```

------------------------------------------------------------------------

# 7. Multiple Assignment

``` python
a, b, c = 10, 20, 30
```

Assign same value:

``` python
x = y = z = 100
```

------------------------------------------------------------------------

# 8. Variable Reassignment

``` python
age = 25
age = 26
```

------------------------------------------------------------------------

# 9. Checking Data Types

``` python
name = "John"
print(type(name))
```

Common types:
<!-- 
-   int
-   float
-   str
-   bool
-   list
-   tuple
-   dict
-   set
-   NoneType -->

------------------------------------------------------------------------

# 10. Variable Naming Rules

Valid:

``` python
name
student_age
_marks
employee1
```

Invalid:

``` python
1name
student name
first-name
class
```

Rules:

-   Start with a letter or `_`
-   May contain letters, digits, `_`
-   Cannot start with a digit
-   No spaces or special characters
-   Cannot use Python keywords

------------------------------------------------------------------------

# 11. Naming Conventions (PEP 8)

Variables:

``` python
first_name
employee_salary
```

Functions:

``` python
def calculate_salary():
    pass
```

Classes:

``` python
class EmployeeDetails:
    pass
```

Constants:

``` python
MAX_USERS = 100
PI = 3.14159
```

------------------------------------------------------------------------

# 12. Reserved Keywords

Examples:

-   if
-   else
-   for
-   while
-   class
-   def
-   return
-   import

------------------------------------------------------------------------

# 13. Case Sensitivity

``` python
name = "John"
Name = "David"
NAME = "Mike"
```

All are different variables.

------------------------------------------------------------------------

# 14. Variable Scope

## Global

``` python
name = "John"

def display():
    print(name)
```

## Local

``` python
def display():
    city = "Chennai"
    print(city)
```

------------------------------------------------------------------------

# 15. Memory Address

``` python
name = "John"
print(id(name))
```

------------------------------------------------------------------------

# 16. Delete Variables

``` python
name = "John"
del name
```

------------------------------------------------------------------------

# 17. Type Casting

``` python
age = "25"
age = int(age)

price = "99.5"
price = float(price)

num = 100
text = str(num)
```

------------------------------------------------------------------------

# 18. Common Data Types

``` python
name = "John"
age = 25
salary = 50000.50
is_active = True
marks = [80, 90, 95]
student = ("Tom", 20)
employee = {"id":101, "name":"John"}
numbers = {1,2,3}
value = None
```

------------------------------------------------------------------------

# 19. Mutable vs Immutable

## Mutable

-   list
-   dict
-   set
-   bytearray

## Immutable

-   int
-   float
-   bool
-   str
-   tuple
-   bytes
-   frozenset
-   range
-   None

------------------------------------------------------------------------

# 20. Real-Time Automation Example

``` python
browser = "Chrome"
base_url = "https://example.com"
username = "admin"
password = "Admin123"
timeout = 30
```

------------------------------------------------------------------------

# 21. Common Mistakes

❌

``` python
student name = "John"
```

✅

``` python
student_name = "John"
```

❌

``` python
1age = 25
```

✅

``` python
age1 = 25
```

