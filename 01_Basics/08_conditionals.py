# 08_conditionals.py
"""
CONDITIONALS (if, elif, else) in Python

We use conditionals to make decisions in code.

This file shows:
- EASY: simple if / else
- MEDIUM: else-if chains, nested conditions
- HIGH: rule-based examples (grading, pricing, access rules)

Run this file to see outputs:
    python 01_Basics/08_conditionals.py
"""

print("\n" + "=" * 60)
print("EASY LEVEL: Basic if / else")
print("=" * 60)

age = 17

if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

number = -5

if number > 0:
    print(number, "is positive")
elif number == 0:
    print(number, "is zero")
else:
    print(number, "is negative")


print("\n" + "=" * 60)
print("MEDIUM LEVEL: Multiple conditions and nesting")
print("=" * 60)

print("\nExample 1: Simple grading (A/B/C/Fail)")
marks = 82

if marks >= 90:
    grade = "A+"
elif marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B"
elif marks >= 60:
    grade = "C"
else:
    grade = "Fail"

print("Marks:", marks, "Grade:", grade)


print("\nExample 2: Nested conditions (age + country rule)")
age = 19
country = "IN"

if country == "IN":
    if age >= 18:
        print("In India, you can vote.")
    else:
        print("In India, you cannot vote yet.")
else:
    print("Country not handled in this simple example.")


print("\nExample 3: Combining conditions with and/or")
temp_c = 35
is_raining = False

if temp_c > 30 and not is_raining:
    print("It's hot and dry. Drink water.")
elif temp_c > 30 and is_raining:
    print("It's hot and raining.")
elif temp_c <= 10:
    print("It's very cold.")
else:
    print("Weather is normal.")


print("\n" + "=" * 60)
print("HIGH / ADVANCED LEVEL: Rule-based conditionals")
print("=" * 60)

print("\nExample 4: E-commerce shipping rules")
"""
Rules:
- If total >= 1000 -> Free shipping
- Else if total >= 500 AND user is premium -> 50% shipping discount
- Else if total >= 500 -> normal shipping
- Else -> small-order surcharge
"""

cart_total = 650
is_premium_user = True
shipping_base = 100

if cart_total >= 1000:
    shipping_cost = 0
elif cart_total >= 500 and is_premium_user:
    shipping_cost = shipping_base * 0.5
elif cart_total >= 500:
    shipping_cost = shipping_base
else:
    shipping_cost = shipping_base + 50  # surcharge

print("Cart total:", cart_total)
print("Premium user:", is_premium_user)
print("Shipping cost:", shipping_cost)


print("\nExample 5: Login security rules")
"""
Rules:
- If wrong_attempts >= 5 -> lock account
- Else if wrong_attempts > 0 -> warn user
- Else -> normal
"""

wrong_attempts = 3

if wrong_attempts >= 5:
    status = "LOCKED"
elif wrong_attempts > 0:
    status = "WARNING"
else:
    status = "OK"

print("Wrong attempts:", wrong_attempts)
print("Account status:", status)


print("\nExample 6: Eligibility decision with multiple factors")
"""
Loan eligibility simple example:
- income >= 50000
- AND credit_score >= 700
- AND (age between 21 and 60)
"""

income = 60000
credit_score = 710
age = 25

if income >= 50000 and credit_score >= 700 and 21 <= age <= 60:
    loan_eligible = True
else:
    loan_eligible = False

print("Income:", income)
print("Credit score:", credit_score)
print("Age:", age)
print("Loan eligible:", loan_eligible)

#//Try it yourself example is High Level
print("Amount:", amount)
print("Country:", country)
print("Night time:", is_night_time)
print("Fraud decision:", decision)


print("\nExample 8: Subscription plan & features")
"""
Decide which features a user gets based on plan and payment status.
Plans: free, pro, enterprise
"""

plan = "pro"
is_payment_current = True

if not is_payment_current:
    features = "No access (payment issue)"
elif plan == "free":
    features = "Basic features only"
elif plan == "pro":
    features = "Pro features + priority support"
elif plan == "enterprise":
    features = "All features + dedicated manager"
else:
    features = "Unknown plan"

print("Plan:", plan)
print("Payment current:", is_payment_current)
print("Available features:", features)


print("\nEnd of conditionals examples.")
