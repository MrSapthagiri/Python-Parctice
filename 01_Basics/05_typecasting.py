
print("\n" + "=" * 60)
print("EASY (Beginner) examples")
print("=" * 60)

# 1) str -> int
age_str = "21"
age_int = int(age_str)  # "21" -> 21
print("age_int:", age_int, type(age_int))

# 2) str -> float
price_str = "99.50"
price_float = float(price_str)  # "99.50" -> 99.5
print("price_float:", price_float, type(price_float))

# 3) int/float -> str
score = 120
score_str = str(score)  # 120 -> "120"
print("score_str:", score_str, type(score_str))

# 4) float -> int (truncation, NOT rounding)
x = 10.99
print("int(10.99):", int(x))  # 10


print("\n" + "=" * 60)
print("MEDIUM (Practical) examples")
print("=" * 60)

print("\nExample A: converting input (basic)")
print("Note: input() always gives a STRING. We must convert it.")

# Uncomment this block to try interactive input
"""
name = input("Name: ")
age_text = input("Age (years): ")
height_text = input("Height (meters): ")

age = int(age_text)
height = float(height_text)

print(f"Hello {name}")
print(f"Next year you will be {age + 1}")
print(f"Your height in cm is {height * 100:.0f} cm")
"""

print("\nExample B: safer conversion using try/except")
user_text = "abc"  # change to "25" to see success
try:
    n = int(user_text)
    print("Converted:", n, "| n + 10 =", n + 10)
except ValueError:
    print(f"Cannot convert {user_text!r} to int (ValueError).")


print("\n" + "=" * 60)
print("COMMON MISTAKES (very important)")
print("=" * 60)

# Mistake 1: bool("False") is True because it's a non-empty string!
print('bool("False"):', bool("False"))
print('bool(""):', bool(""))

# Safe pattern for yes/no text -> boolean
text = "yes"  # try "No", "TRUE", "0", ""
as_bool = text.strip().lower() in ("y", "yes", "true", "1")
print(f"safe text->bool for {text!r}:", as_bool)

# Mistake 2: int("10.5") fails because it's not an integer string
try:
    print(int("10.5"))
except ValueError:
    print('int("10.5") fails -> convert to float first, then int:')
    print("int(float('10.5')) =", int(float("10.5")))


print("\n" + "=" * 60)
print("ADVANCED / 'LOW-LEVEL' style examples")
print("=" * 60)

print("\nExample 1: base conversion (binary/hex strings -> int)")
print('int("1010", 2):', int("1010", 2))  # 10
print('int("ff", 16):', int("ff", 16))    # 255
print("bin(10):", bin(10))
print("hex(255):", hex(255))

print("\nExample 2: list/tuple/set conversions")
nums = [1, 2, 2, 3]
print("original list:", nums)
print("set(nums) removes duplicates:", set(nums))
print("tuple(nums):", tuple(nums))

print("\nExample 3: custom type conversion with __int__/__float__/__str__")


class TemperatureC:
    def __init__(self, c):
        self.c = float(c)

    def __str__(self):
        return f"{self.c}°C"

    def __float__(self):
        return self.c

    def __int__(self):
        return int(self.c)  # truncation


t = TemperatureC("36.6")
print("str(t):", str(t))
print("float(t):", float(t))
print("int(t):", int(t))

print("\nExample 4: truncation vs rounding")
y = 10.6
print("int(10.6):", int(y))      # 10 (truncation)
print("round(10.6):", round(y))  # 11 (rounding)
print("round(10.5):", round(10.5))  # banker's rounding in Python
