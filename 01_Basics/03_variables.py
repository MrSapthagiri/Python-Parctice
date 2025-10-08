# 03_variables.py
# ======================================================
#  LOW LEVEL (Basic Variables)
# ======================================================

# Assigning values
x = 10
y = 3.14
name = "Alice"
is_active = True

print("x:", x)
print("y:", y)
print("name:", name)
print("is_active:", is_active)

# Multiple assignment
a, b, c = 1, 2, 3
print("a:", a, "b:", b, "c:", c)

# Same value assignment
m = n = 100
print("m:", m, "n:", n)

# Type checking
print(type(x), type(y), type(name), type(is_active))


# ======================================================
#  MEDIUM LEVEL (Operations & Casting)
# ======================================================

# Arithmetic operations
num1 = 15
num2 = 4
print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)
print("Division:", num1 / num2)
print("Floor Division:", num1 // num2)
print("Modulus:", num1 % num2)
print("Power:", num1 ** num2)

# Type conversion
int_val = int("20")       # string → int
float_val = float("5.5")  # string → float
str_val = str(100)        # int → string
bool_val = bool(0)        # 0 → False, non-zero → True
print(int_val, float_val, str_val, bool_val)

# f-strings
age = 25
print(f"My name is {name} and I am {age} years old.")


# ======================================================
#  HIGH LEVEL (Advanced Variable Usage)
# ======================================================

"""
Demonstrating advanced variable usage:
- Constants
- Global vs Local variables
- Mutable vs Immutable types
- Variable scope
"""

# Constant (by convention, constants are in UPPERCASE)
PI = 3.14159
print("PI:", PI)

# Global and Local variables
count = 0  # global variable

def increment():
    """
    Demonstrate local vs global variables.
    """
    global count
    count += 1
    return count

print("Global count after increment:", increment())
print("Global count after increment:", increment())

# Mutable vs Immutable
immutable_num = 10
mutable_list = [1, 2, 3]

immutable_num += 5  # creates new int object
mutable_list.append(4)  # modifies same list object

print("Immutable Num:", immutable_num)
print("Mutable List:", mutable_list)

# Deleting variables
temp = "temporary"
print("Before delete:", temp)
del temp
# print(temp)  # would raise NameError

# Unpacking with *
numbers = [1, 2, 3, 4, 5]
first, *middle, last = numbers
print("First:", first, "Middle:", middle, "Last:", last)

# Variable scope in nested functions
