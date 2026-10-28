"""
MODULE 7.5: LOOPING THROUGH LISTS

DEFINITION
Iteration visits list items one at a time. Use a for loop when processing each
value; use enumerate() when you also need its position.

SYNTAX
    for item in values:
        print(item)

    for index, item in enumerate(values, start=0):
        print(index, item)

FLOWCHART: PROCESS EACH ITEM
    [Start loop]
       |
       v
    [More items?] -- No --> [Finish]
       |
      Yes
       |
       v
    [Get next item (and optional index)]
       |
       v
    [Process, count, or filter item]
       |
       +-----------------------> [Check for more items]
"""

print("Example 1: Visit every item")
products = ["tea", "rice", "beans"]
for product in products:
    print(f"Product: {product}")

print("\nExample 2: Use enumerate() for positions")
for index, product in enumerate(products, start=1):
    print(f"{index}. {product}")

print("\nExample 3: Build a total")
prices = [3.50, 2.25, 4.00]
total = 0.0
for price in prices:
    total += price
print(f"Total: ${total:.2f}")

print("\nExample 4: Filter values into a new list")
temperatures = [18, 31, 24, 35, 20]
hot_days = []
for temperature in temperatures:
    if temperature >= 30:
        hot_days.append(temperature)
print(hot_days)

print("\nExample 5: Search and stop when found")
user_ids = [104, 207, 315, 422]
target_id = 315
for user_id in user_ids:
    if user_id == target_id:
        print(f"Found user {target_id}.")
        break
else:
    print(f"User {target_id} was not found.")

print("\nExample 6: any() and all()")
scores = [76, 82, 91]
print(any(score < 50 for score in scores))  # Any failing score? False
print(all(score >= 50 for score in scores))  # All passing? True

# If removing items while iterating, build a new filtered list instead.
