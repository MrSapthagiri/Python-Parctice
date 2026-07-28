# Python Data Types - Complete Guide

## Table of Contents

1.  What is a Data Type?
2.  Why Data Types are Important
3.  Categories of Data Types
4.  Numeric Data Types
5.  Text Data Type
6.  Sequence Data Types
7.  Mapping Data Type
8.  Set Data Types
9.  Boolean Data Type
10. Binary Data Types
11. None Data Type
12. Mutable vs Immutable
13. Type Conversion (Casting)
14. Checking Data Type
15. Memory Representation
16. Real-Time Examples
17. Common Mistakes

------------------------------------------------------------------------

# 1. What is a Data Type?

A **data type** defines the type of value a variable can store. It tells
Python how to store, process, and manipulate data.

**Interview Definition**

> A data type specifies the kind of value a variable holds. Python
> automatically determines the data type based on the assigned value.

``` python
age = 25
salary = 50000.50
name = "John"
```

------------------------------------------------------------------------

# 2. Why Data Types are Important

-   Store data efficiently
-   Perform valid operations
-   Improve readability
-   Reduce programming errors
-   Improve application performance

``` python
age = 25
name = "John"

print(age + 5)
print(name + " Doe")
```

------------------------------------------------------------------------

# 3. Categories of Python Data Types

  Category   Data Types
  ---------- ------------------------------
  Numeric    int, float, complex
  Text       str
  Sequence   list, tuple, range
  Mapping    dict
  Set        set, frozenset
  Boolean    bool
  Binary     bytes, bytearray, memoryview
  None       NoneType

------------------------------------------------------------------------

# 4. Numeric Data Types

## Integer (`int`)

``` python
age = 25
marks = -90
print(type(age))
```

## Float (`float`)

``` python
price = 99.99
height = 5.8
```

## Complex (`complex`)

``` python
number = 3 + 4j
print(number)
print(type(number))
```

------------------------------------------------------------------------

# 5. String (`str`)

``` python
name = "Santhosh"
print(type(name))
```

Strings can use:

``` python
"Hello"
'Hello'
"""Hello"""
'''Hello'''
```

------------------------------------------------------------------------

# 6. Sequence Data Types

## List

-   Ordered
-   Mutable
-   Allows duplicates

``` python
fruits = ["Apple", "Orange", "Mango"]
fruits.append("Banana")
```

## Tuple

-   Ordered
-   Immutable
-   Allows duplicates

``` python
colors = ("Red", "Blue", "Green")
```

## Range

``` python
for i in range(5):
    print(i)
```

------------------------------------------------------------------------

# 7. Dictionary (`dict`)

``` python
student = {
    "name": "John",
    "age": 22,
    "city": "Chennai"
}

print(student["name"])
```

------------------------------------------------------------------------

# 8. Set Data Types

## Set

``` python
numbers = {1, 2, 3, 3}
print(numbers)
```

## Frozen Set

``` python
numbers = frozenset({1, 2, 3})
```

------------------------------------------------------------------------

# 9. Boolean (`bool`)

``` python
is_active = True
is_admin = False
```

------------------------------------------------------------------------

# 10. Binary Data Types

``` python
data = b"Hello"
buffer = bytearray(5)
view = memoryview(bytes(5))
```

------------------------------------------------------------------------

# 11. NoneType

``` python
value = None
print(type(value))
```

------------------------------------------------------------------------

# 12. Mutable vs Immutable

## Mutable

-   list
-   dict
-   set
-   bytearray

## Immutable

-   int
-   float
-   complex
-   str
-   tuple
-   bool
-   bytes
-   frozenset
-   range
-   NoneType

------------------------------------------------------------------------

# 13. Type Casting

``` python
age = int("25")
price = float("99.99")
text = str(100)
letters = list("Python")
```

------------------------------------------------------------------------

# 14. Checking Data Type

``` python
name = "John"
print(type(name))
```

------------------------------------------------------------------------

# 15. Memory Representation

``` python
name = "John"
print(id(name))
```

------------------------------------------------------------------------

# 16. Real-Time Automation Example

``` python
browser = "Chrome"
base_url = "https://example.com"
timeout = 30
is_logged_in = True

headers = {
    "Content-Type": "application/json"
}
```

------------------------------------------------------------------------

# 17. Common Mistakes

❌

``` python
age = "25"
print(age + 5)
```

✅

``` python
age = int(age)
print(age + 5)
```

