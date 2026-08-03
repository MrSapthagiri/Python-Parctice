"""Python Operator Examples and Explanation

Module 3: Operators
Topics covered:
- Arithmetic Operators
- Assignment Operators
- Comparison Operators
- Logical Operators
- Identity Operators (is, is not)
- Membership Operators (in, not in)
- Operator Precedence

This file includes definitions, sample code, and high-impact idioms.
"""
print("*****************************Arithmetic examples:*****************************")
# ------------------------------------------------------------
# Arithmetic Operators
# ------------------------------------------------------------
# Definition: Perform numeric calculations and work with sequences.
# Common operators: + - * / // % **

x = 10
y = 3
print("Arithmetic examples:")
print("x + y =", x + y)        # 13
print("x - y =", x - y)        # 7
print("x * y =", x * y)        # 30
print("x / y =", x / y)        # 3.3333333333333335
print("x // y =", x // y)      # 3  (floor division)
print("x % y =", x % y)        # 1  (remainder)
print("x ** y =", x ** y)      # 1000 (exponentiation)

# High-impact example: convert seconds into hours, minutes and seconds.
seconds = 3665
hours = seconds // 3600
minutes = (seconds % 3600) // 60
secs = seconds % 60
print("Time conversion:", hours, "hours", minutes, "minutes", secs, "seconds")

# High-impact example: compound interest formula.
principal = 1000
rate = 0.05
years = 10
future_value = principal * ((1 + rate) ** years)
print("Compound interest after", years, "years:", round(future_value, 2))

print("*****************************Assignment Operators*****************************")

# ------------------------------------------------------------
# Assignment Operators
# ------------------------------------------------------------
# Definition: Bind values to variables and optionally combine update operations.
# Common operators: =, +=, -=, *=, /=, //=, %=, **=

count = 5
print("Initial count:", count)
count += 2  # same as count = count + 2
print("After += 2:", count)
count *= 3  # same as count = count * 3
print("After *= 3:", count)

# Augmented assignment with mutable types may change the object in place.
items = [1, 2]
print("Original items id:", id(items))
items += [3]
print("Items after +=:", items, "id:", id(items))

# For immutables, augmented assignment rebinds the name.
number = 7
print("Original number id:", id(number))
number += 1
print("Number after += 1:", number, "id:", id(number))

print("*****************************Comparison Operators*****************************")
# ------------------------------------------------------------
# Comparison Operators
# ------------------------------------------------------------
# Definition: Compare values and return a boolean result.
# Common operators: ==, !=, <, >, <=, >=

print("Comparison examples:")
print("10 == 3 ->", 10 == 3)
print("10 != 3 ->", 10 != 3)
print("3 < 10 ->", 3 < 10)
print("3 <= 3 ->", 3 <= 3)
print("3 > 10 ->", 3 > 10)
print("3 >= 10 ->", 3 >= 10)

# Chained comparisons are concise and readable.
score = 75
print("50 <= score < 100 ->", 50 <= score < 100)

# High-impact example: filter values using comparison.
ages = [12, 25, 19, 40, 17]
adults = [age for age in ages if age >= 18]
print("Adults:", adults)

print("*****************************Logical Operators*****************************")

# ------------------------------------------------------------
# Logical Operators
# ------------------------------------------------------------
# Definition: Combine boolean expressions.
# Operators: and, or, not
# Python uses short-circuit evaluation.

print("Logical examples:")
print("True and False ->", True and False)
print("True or False ->", True or False)
print("not True ->", not True)

# and returns the first falsy operand or the last value if all are truthy.
print("0 and 5 ->", 0 and 5)
print("5 and 0 ->", 5 and 0)
print("5 and 7 ->", 5 and 7)

# or returns the first truthy operand or the last value if none are truthy.
print("0 or 5 ->", 0 or 5)
print("5 or 0 ->", 5 or 0)
print("0 or None ->", 0 or None)

# High-impact pattern: default values.
user_input = ""
display_name = user_input or "Anonymous"
print("Display name fallback:", display_name)

# Guard evaluation with and to avoid errors.
obj = None
result = obj and obj.get("key")
print("Result when obj is None:", result)

# Avoid this if a valid value can be falsy.
valid_zero = 0
fallback = valid_zero or 99
print("Fallback with falsy valid value:", fallback)

# ------------------------------------------------------------
# Identity Operators
# ------------------------------------------------------------
# Definition: Test whether two names refer to the same object.
# Operators: is, is not

a = [1, 2]
b = a
c = [1, 2]
print("a is b ->", a is b)
print("a is c ->", a is c)
print("a == c ->", a == c)

# Correct singleton check for None.
value = None
if value is None:
    print("value is None")

# Pitfall: do not use is for numeric equality checks.
x = 256
y = 256
print("x is y (may be True because of interning):", x is y)

print("*****************************Membership Operators*****************************")

# ------------------------------------------------------------
# Membership Operators
# ------------------------------------------------------------
# Definition: Test membership in a sequence, set, tuple, or dictionary keys.
# Operators: in, not in

text = "hello"
print("'e' in text ->", 'e' in text)
print("'x' not in text ->", 'x' not in text)

numbers = [1, 2, 3, 4]
print("3 in numbers ->", 3 in numbers)

config = {'host': 'localhost', 'port': 8080}
print("'port' in config ->", 'port' in config)

# High-impact pattern: fast membership tests with a set.
allowed_extensions = {'jpg', 'png', 'gif'}
filename = "photo.PNG"
extension = filename.split('.')[-1].lower()
print("Allowed extension ->", extension in allowed_extensions)

# Remove duplicates while preserving order.
items = [5, 2, 5, 3, 2, 7]
seen = set()
unique_items = []
for item in items:
    if item not in seen:
        seen.add(item)
        unique_items.append(item)
print("Unique items preserving order:", unique_items)

print("*****************************Operator Precedence*****************************")

# ------------------------------------------------------------
# Operator Precedence
# ------------------------------------------------------------
# Definition: Rules that determine the order of evaluation in expressions.
# Example precedence from highest to lowest for common operators:
# 1. ()
# 2. **
# 3. unary +, -
# 4. *, /, //, %
# 5. +, -
# 6. <<, >>
# 7. &
# 8. ^
# 9. |
# 10. comparisons, is, in
# 11. not
# 12. and
# 13. or

value = 2 + 3 * 4 ** 2
# Evaluate: 4 ** 2 = 16, 3 * 16 = 48, 2 + 48 = 50
print("Precedence example 2 + 3 * 4 ** 2 ->", value)

value2 = (2 + 3) * 4 ** 2
# Evaluate: (2 + 3) = 5, 4 ** 2 = 16, 5 * 16 = 80
print("With parentheses (2 + 3) * 4 ** 2 ->", value2)

# ------------------------------------------------------------
# Practical examples and exercise answers
# ------------------------------------------------------------

# Swap values without a temporary variable.
first = "apple"
second = "banana"
first, second = second, first
print("After swap:", first, second)

# Conditional expression using comparison.
score = 75
print("Pass" if 50 <= score < 100 else "Fail")

# Case-insensitive membership check.
names = ["Alison", "Jason", "Sam", "SONIA"]
matching = [name for name in names if "son" in name.lower()]
print("Names containing 'son':", matching)

# One-line safe method call using short-circuiting.
obj = {'value': 10}
output = obj and obj.get('value')
print("Safe access using and:", output)

# When obj can be None and you need explicit non-None guard.
obj = None
if obj is not None:
    print(obj.get('value'))

# ------------------------------------------------------------
# Exercise demonstrations
# ------------------------------------------------------------
print("Exercise 1 output:", 5 / 2, 5 // 2, 5 % 2, 5 ** 2)
print("Exercise 2 swap:", (lambda x, y: (y, x))(1, 2))
print("Exercise 3 mutable list identity:")
list_x = []
list_y = list_x
list_x += [1]
print(list_x, list_y)
print("Exercise 4 None check:", None is None)
print("Exercise 5 range check:", 50 <= 75 < 100)
print("Exercise 6 precedence result:", 2 + 3 * 4 ** 2)

# High-impact operator summary.
print("Operator groups: arithmetic, assignment, comparison, logical, identity, membership")
