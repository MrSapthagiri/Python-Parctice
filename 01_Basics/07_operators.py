# 07_operators.py
"""
OPERATORS in Python

This file shows examples of:
- Arithmetic operators (+, -, *, /, //, %, **)
- Comparison operators (==, !=, >, <, >=, <=)
- Logical operators (and, or, not)
- Assignment operators (+=, -=, etc.)
- Bitwise operators (&, |, ^, <<, >>)  [a bit more advanced]

Sections:
- EASY: very simple arithmetic and comparison
- MEDIUM: small practical examples
- HIGH / ADVANCED: combining operators and bitwise examples

Run this file to see outputs:
    python 01_Basics/07_operators.py
"""

print("\n" + "=" * 60)
print("EASY LEVEL: Basic arithmetic and comparison")
print("=" * 60)

a = 10
b = 3

# Arithmetic (focus on addition first)
print("a =", a, "b =", b)
print("Addition a + b =", a + b)
print("Subtraction a - b =", a - b)
print("Multiplication a * b =", a * b)
print("Division a / b =", a / b)      # float division
print("Floor division a // b =", a // b)  # integer division (quotient)
print("Remainder a % b =", a % b)    # modulus (remainder)
print("Power a ** b =", a ** b)      # exponent

# Comparison operators return True / False
print("\nComparison examples:")
print("a == b:", a == b)
print("a != b:", a != b)
print("a > b:", a > b)
print("a < b:", a < b)
print("a >= b:", a >= b)
print("a <= b:", a <= b)


print("\n" + "=" * 60)
print("MEDIUM LEVEL: Logical + assignment in small examples")
print("=" * 60)

age = 20
has_id = True

print("\nLogical operators with conditions:")
print("Age =", age, "Has ID =", has_id)
can_enter_club = (age >= 18) and has_id
print("Can enter club (age>=18 AND has_id):", can_enter_club)

is_child_or_senior = (age < 12) or (age >= 60)
print("Is child OR senior:", is_child_or_senior)

print("not has_id:", not has_id)

# Assignment operators
print("\nAssignment operators:")
count = 0
print("Initial count:", count)
count = count + 1
print("After count = count + 1:", count)
count += 5  # same as count = count + 5
print("After count += 5:", count)
count -= 2
print("After count -= 2:", count)
count *= 3
print("After count *= 3:", count)
count //= 4
print("After count //= 4:", count)

print("\nPractical mini-example (marks and pass/fail):")
marks = 75
is_pass = marks >= 40
is_distinction = marks >= 75
print("Marks:", marks)
print("Passed:", is_pass)
print("Distinction:", is_distinction)


print("\n" + "=" * 60)
print("HIGH / ADVANCED LEVEL: combining operators")
print("=" * 60)

print("\nExample 1: Complex expression")
# Priority (PEMDAS/BODMAS): (), **, *, /, //, %, +, -
x = 5
y = 2
z = 3

result = x + y * z        # 5 + (2 * 3) = 11
print("x + y * z =", result)

result2 = (x + y) * z     # (5 + 2) * 3 = 21
print("(x + y) * z =", result2)

result3 = x ** y ** z     # x ** (y ** z) = 5 ** (2**3) = 5**8
print("x ** y ** z =", result3)


print("\nExample 2: Chained comparisons")
num = 15
print("num =", num)
print("10 < num < 20:", 10 < num < 20)     # True if num between 10 and 20
print("num % 2 == 0:", num % 2 == 0)       # even check
print("num % 2 != 0:", num % 2 != 0)       # odd check


print("\nExample 3: Bitwise operators (low-level style)")
"""
Bitwise operators work on the binary representation of integers.

&  AND  : bit is 1 only if both bits are 1
|  OR   : bit is 1 if at least one bit is 1
^  XOR  : bit is 1 if bits are different
<< LEFT SHIFT : shift bits left (multiply by 2 each time)
>> RIGHT SHIFT: shift bits right (floor divide by 2 each time)
"""

p = 6   # binary:  110
q = 3   # binary:  011

print("p =", p, "binary:", bin(p))
print("q =", q, "binary:", bin(q))

print("p & q (AND):", p & q, "binary:", bin(p & q))   # 010 (2)
print("p | q (OR):", p | q, "binary:", bin(p | q))    # 111 (7)
print("p ^ q (XOR):", p ^ q, "binary:", bin(p ^ q))   # 101 (5)

print("p << 1:", p << 1, "binary:", bin(p << 1))      # 1100 (12)
print("p >> 1:", p >> 1, "binary:", bin(p >> 1))      # 11 (3)


print("\nExample 4: Using operators in a small decision")

salary = 50000
experience_years = 4

eligible_for_promotion = (salary >= 40000 and experience_years >= 3)
print("Salary:", salary)
print("Experience (years):", experience_years)
print("Eligible for promotion:", eligible_for_promotion)


print("\nExample 5 (High impact): E‑commerce discount rules")
"""
Simple rule engine using operators.
"""
cart_total = 1200          # total amount in cart
is_first_order = True
has_coupon = False

# Rule:
# - If cart >= 1000 AND first order -> 20% discount
# - else if cart >= 500 OR has coupon -> 10% discount
# - else -> no discount

if cart_total >= 1000 and is_first_order:
    discount_rate = 0.20
elif cart_total >= 500 or has_coupon:
    discount_rate = 0.10
else:
    discount_rate = 0.0

discount_amount = cart_total * discount_rate
final_amount = cart_total - discount_amount

print("\n[Discount rule example]")
print("Cart total:", cart_total)
print("First order:", is_first_order)
print("Has coupon:", has_coupon)
print("Discount rate:", discount_rate)
print("Final amount to pay:", final_amount)


print("\nExample 6 (High impact): Access control with bit flags")
"""
Use bitwise operators to manage permissions.
"""
READ = 1      # 001
WRITE = 2     # 010
DELETE = 4    # 100

# user with read + write
user_perms = READ | WRITE   # 001 | 010 = 011

can_read = (user_perms & READ) != 0
can_write = (user_perms & WRITE) != 0
can_delete = (user_perms & DELETE) != 0

print("\n[Access control example]")
print("user_perms (binary):", bin(user_perms))
print("Can read:", can_read)
print("Can write:", can_write)
print("Can delete:", can_delete)


print("\nEnd of operators examples.")
