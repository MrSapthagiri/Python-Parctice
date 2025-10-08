# 02_comments_docstrings.py
# -----------------------------------
# Low-Level (Basic) Comments
# -----------------------------------

# This is a single-line comment
print("Hello, World!")  # This prints text

"""
This is a 
multi-line comment
used for quick notes
"""

# -----------------------------------
# Medium-Level (Functions with Docstrings)
# -----------------------------------

def add(a, b):
    """
    Add two numbers and return the result.

    Parameters:
        a (int or float): first number
        b (int or float): second number

    Returns:
        int or float: sum of a and b
    """
    return a + b

print("Sum:", add(5, 3))


class Person:
    """
    A simple Person class example.

    Attributes:
        name (str): person's name
        age (int): person's age
    """

    def __init__(self, name, age):
        """
        Initialize Person object.

        Args:
            name (str): person's name
            age (int): person's age
        """
        self.name = name
        self.age = age

    def greet(self):
        """Return a greeting message."""
        return f"Hello, I am {self.name}."


p = Person("Alice", 25)
print(p.greet())


# -----------------------------------
# High-Level (Module, Documentation, Professional Style)
# -----------------------------------

"""
Module: comments_docstrings
Author: Your Name
Description:
    This module demonstrates Python comments and docstrings
    at different levels (low, medium, high).
    It follows best practices for documentation.
"""

def factorial(n):
    """
    Calculate factorial using recursion.

    Args:
        n (int): Non-negative integer

    Returns:
        int: factorial of n

    Raises:
        ValueError: if n is negative
    """
    if n < 0:
        raise ValueError("Negative numbers not allowed")
    return 1 if n in (0, 1) else n * factorial(n - 1)


print("Factorial 5:", factorial(5))


# ======================================================
#  LOW LEVEL (Basic Comments)
# ======================================================

# Single-line comment
print("Hello, World!")  # Inline comment

"""
Multi-line comment
can be used for
quick explanations
"""

# Example: simple math
a = 10
b = 5
# Adding numbers
c = a + b
print("Sum:", c)


# ======================================================
#  MEDIUM LEVEL (Functions & Classes with Docstrings)
# ======================================================

def multiply(x, y):
    """
    Multiply two numbers.

    Args:
        x (int or float): first number
        y (int or float): second number

    Returns:
        int or float: product of x and y
    """
    return x * y

print("Product:", multiply(4, 3))


def greet_user(name="Guest"):
    """
    Greet a user with their name.

    Args:
        name (str): user name (default = "Guest")

    Returns:
        str: greeting message
    """
    return f"Welcome, {name}!"

print(greet_user("Alice"))


class Calculator:
    """
    A basic Calculator class with simple operations.
    """

    def add(self, a, b):
        """Return the sum of a and b."""
        return a + b

    def subtract(self, a, b):
        """Return the difference of a and b."""
        return a - b

    def multiply(self, a, b):
        """Return the product of a and b."""
        return a * b

    def divide(self, a, b):
        """
        Divide a by b.

        Raises:
            ZeroDivisionError: if b = 0
        """
        if b == 0:
            raise ZeroDivisionError("Division by zero not allowed")
        return a / b


calc = Calculator()
print("Calc Add:", calc.add(10, 5))
print("Calc Divide:", calc.divide(10, 2))


# ======================================================
#  HIGH LEVEL (Module Docstrings + Advanced Functions)
# ======================================================

"""
Module: 02_comments_docstrings
Author: Your Name
Description:
    This module demonstrates different levels of
    comments and docstrings in Python.

Levels:
    - Low: Basic inline & block comments
    - Medium: Functions & class docstrings
    - High: Module-level docs, detailed error handling
"""

def fibonacci(n):
    """
    Generate Fibonacci sequence up to n terms.

    Args:
        n (int): number of terms

    Returns:
        list: Fibonacci sequence as a list

    Raises:
        ValueError: if n <= 0
    """
    if n <= 0:
        raise ValueError("n must be a positive integer")
    seq = [0, 1]
    for i in range(2, n):
        seq.append(seq[-1] + seq[-2])
    return seq[:n]


def file_reader(filename):
    """
    Read the contents of a file.

    Args:
        filename (str): path to the file

    Returns:
        str: file content as string

    Raises:
        FileNotFoundError: if file does not exist
    """
    try:
        with open(filename, "r") as f:
            return f.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"{filename} not found.")


print("Fibonacci (first 7):", fibonacci(7))

# Example try-except with docstring documented function
try:
    print(file_reader("not_existing.txt"))
except Exception as e:
    print("Error:", e)
# Example try-except-finally