"""
SORTING LISTS - 30 EXAMPLES

DEFINITION
Sorting arranges values in an order. Python provides:
- sorted(values): returns a new sorted list and keeps the original unchanged.
- values.sort(): sorts the list itself and returns None.

SYNTAX
    ordered = sorted(values)
    ordered = sorted(values, reverse=True)
    ordered = sorted(values, key=len)
    values.sort()
    values.sort(key=some_function, reverse=True)

IMPORTANT IDEAS
- Numbers sort numerically; strings sort alphabetically by Unicode order.
- Use key= to choose the value Python should compare.
- Use reverse=True for descending order.
- Python sorting is stable: equal keys keep their previous relative order.
- Avoid mixing incomparable types such as integers and strings without a key.
- Prefer sorted() when you need to preserve the original list.

FLOWCHART
    [Need to arrange values?]
               |
               v
    [Keep the original list unchanged?]
        | Yes                 | No
        v                     v
    [Use sorted()]        [Use list.sort()]
        |                     |
        +----------+----------+
                   |
                   v
       [Need custom comparison?]
                   |
             Yes   v
       [Choose key= function]
                   |
                   v
          [Need descending order?]
                   |
             Yes   v
          [Set reverse=True]
                   |
                   v
          [Use sorted result]

Run this file to see all 30 examples. They progress from simple built-in
sorting to custom keys, stable sorting, and a small reusable sorting function.
"""

print("=" * 64)
print("BEGINNER: BASIC SORTING")
print("=" * 64)

# Example 1: Sort numbers from smallest to largest.
# sorted() creates a new list; the original list is not changed.
numbers = [8, 3, 10, 1, 6]
print("\n1. Numbers ascending:", sorted(numbers))
print("   Original numbers: ", numbers)

# Example 2: Sort numbers from largest to smallest.
# reverse=True reverses the sort order.
print("\n2. Numbers descending:", sorted(numbers, reverse=True))

# Example 3: Sort words alphabetically.
animals = ["tiger", "cat", "elephant", "dog"]
print("\n3. Animals alphabetically:", sorted(animals))

# Example 4: Sort words in reverse alphabetical order.
print("\n4. Animals reverse alphabetically:", sorted(animals, reverse=True))

# Example 5: Sort the original list in place.
# sort() changes animals_in_order directly.
animals_in_order = ["tiger", "cat", "elephant", "dog"]
animals_in_order.sort()
print("\n5. List after sort():", animals_in_order)

# Example 6: sort() returns None.
# The list changes, but the return value is not a sorted list.
tasks = ["write", "plan", "review"]
sort_result = tasks.sort()
print("\n6. Changed list:", tasks)
print("   Return from sort():", sort_result)

# Example 7: Sort words by length.
# key=len compares the length of each word instead of the word itself.
words = ["watermelon", "fig", "apple", "kiwi"]
print("\n7. Words by length:", sorted(words, key=len))

# Example 8: Sort text without uppercase/lowercase affecting the order.
# str.casefold() is useful for case-insensitive text comparisons.
names = ["zoe", "Ari", "maya", "Bea"]
print("\n8. Names ignoring case:", sorted(names, key=str.casefold))

# Example 9: Sort numbers stored as strings numerically.
# Without key=int, text like "100" would be ordered before "20".
number_text = ["100", "20", "3", "45"]
print("\n9. Numeric string order:", sorted(number_text, key=int))

# Example 10: Sort by absolute value.
# abs() compares distance from zero, not whether a number is negative.
measurements = [-9, 2, -4, 7, 0]
print("\n10. By distance from zero:", sorted(measurements, key=abs))

print("\n" + "=" * 64)
print("INTERMEDIATE: CUSTOM KEYS AND REAL DATA")
print("=" * 64)

# Example 11: Sort words from longest to shortest.
words = ["tea", "chocolate", "bread", "rice"]
print("\n11. Longest words first:", sorted(words, key=len, reverse=True))

# Example 12: Sort tuples by their first value.
# Tuples sort naturally by first item, then later items if needed.
coordinates = [(4, 2), (1, 9), (3, 5)]
print("\n12. Coordinates by x value:", sorted(coordinates))

# Example 13: Sort records by a dictionary field.
# The lambda function selects each product's price as the sort key.
products = [
    {"name": "Notebook", "price": 3.50},
    {"name": "Pencil", "price": 0.80},
    {"name": "Folder", "price": 2.25},
]
by_price = sorted(products, key=lambda product: product["price"])
print("\n13. Products from cheapest to most expensive:")
for product in by_price:
    print(f"   {product['name']}: ${product['price']:.2f}")

# Example 14: Sort products by price from highest to lowest.
by_price_highest = sorted(
    products, key=lambda product: product["price"], reverse=True
)
print("\n14. Products from most expensive to cheapest:")
for product in by_price_highest:
    print(f"   {product['name']}: ${product['price']:.2f}")

# Example 15: Sort students by score.
students = [("Ari", 91), ("Bea", 82), ("Chen", 88)]
by_score = sorted(students, key=lambda student: student[1], reverse=True)
print("\n15. Students by highest score:", by_score)

# Example 16: Sort by multiple fields at once.
# The key is a tuple: department first, then name.
employees = [
    {"name": "Mina", "department": "Design"},
    {"name": "Ari", "department": "Engineering"},
    {"name": "Bea", "department": "Design"},
]
by_department_name = sorted(
    employees, key=lambda employee: (employee["department"], employee["name"])
)
print("\n16. Employees by department, then name:")
for employee in by_department_name:
    print(f"   {employee['department']}: {employee['name']}")

# Example 17: Sort by the last character.
# A key can be any small function that returns comparable values.
words = ["camera", "lamp", "book", "cup"]
print("\n17. Words by last letter:", sorted(words, key=lambda word: word[-1]))

# Example 18: Use a named key function for clarity.
def price_of(product):
    """Return a product's price for sorting."""
    return product["price"]


print("\n18. Product prices using a named key:")
print([product["name"] for product in sorted(products, key=price_of)])

# Example 19: Sort dates in ISO format.
# YYYY-MM-DD strings sort chronologically when all dates use this format.
dates = ["2026-10-28", "2025-01-05", "2026-02-14"]
print("\n19. ISO dates in time order:", sorted(dates))

# Example 20: Sort while placing missing values last.
# Return a tuple: first the missing-value flag, then the actual value.
ratings = [4.5, None, 3.0, 5.0, None]
ratings_sorted = sorted(ratings, key=lambda rating: (rating is None, rating or 0))
print("\n20. Ratings with missing values last:", ratings_sorted)

# Example 21: Sort values by how often they occur.
# count() supplies the key; ties keep their original relative order.
votes = ["blue", "red", "blue", "green", "red", "blue"]
by_frequency = sorted(votes, key=votes.count, reverse=True)
print("\n21. Colors from most common to least:", by_frequency)

# Example 22: Sort by a calculated value.
# This arranges distances by the square of each distance from the origin.
distances = [5, 2, 8, 3]
print("\n22. Distances by squared distance:", sorted(distances, key=lambda d: d**2))

print("\n" + "=" * 64)
print("HIGHER LEVEL: STABILITY, RANKING, AND REUSE")
print("=" * 64)

# Example 23: Stable sort preserves the order of tied items.
# Ari and Chen both have 90 points, so Ari stays before Chen.
students = [("Ari", 90), ("Bea", 82), ("Chen", 90), ("Drew", 82)]
by_score = sorted(students, key=lambda student: student[1], reverse=True)
print("\n23. Stable score order:", by_score)

# Example 24: Sort by two criteria with an explicit tie-breaker.
# Highest score comes first; names break ties alphabetically.
students = [("Chen", 90), ("Ari", 90), ("Bea", 82)]
ranked_students = sorted(students, key=lambda student: (-student[1], student[0]))
print("\n24. Score descending, name ascending:", ranked_students)

# Example 25: Sort by multiple criteria in stages.
# Stable sorting lets us sort by secondary key first, then primary key.
students = [
    {"name": "Ari", "class": "B", "score": 90},
    {"name": "Bea", "class": "A", "score": 90},
    {"name": "Chen", "class": "A", "score": 82},
]
students_by_name = sorted(students, key=lambda student: student["name"])
students_by_class_then_score = sorted(
    students_by_name, key=lambda student: (student["class"], -student["score"])
)
print("\n25. Students by class then score:")
for student in students_by_class_then_score:
    print(f"   {student['class']} - {student['name']}: {student['score']}")

# Example 26: Get the top three values.
# Sort descending, then slice the first three results.
sales = [120, 450, 300, 210, 510, 390]
top_three = sorted(sales, reverse=True)[:3]
print("\n26. Top three sales:", top_three)

# Example 27: Sort a list of dictionaries without changing its input order.
inventory = [
    {"item": "Pen", "quantity": 12},
    {"item": "Book", "quantity": 5},
    {"item": "Ruler", "quantity": 8},
]
inventory_by_quantity = sorted(inventory, key=lambda item: item["quantity"])
print("\n27. Inventory by quantity:", inventory_by_quantity)
print("    Original inventory:", inventory)

# Example 28: Sort unique values.
# A set removes duplicates; sorted() turns them into an ordered list.
measurements = [8, 3, 8, 1, 3, 5]
unique_sorted = sorted(set(measurements))
print("\n28. Unique measurements in order:", unique_sorted)

# Example 29: Implement bubble sort to understand a sorting algorithm.
# This is for learning; Python's built-in sort is faster and preferred in real
# applications. Each pass moves the largest unsorted value toward the end.
def bubble_sort(values):
    """Return a sorted copy using the beginner-friendly bubble sort method."""
    result = values.copy()
    for end in range(len(result) - 1, 0, -1):
        swapped = False
        for index in range(end):
            if result[index] > result[index + 1]:
                result[index], result[index + 1] = result[index + 1], result[index]
                swapped = True
        if not swapped:
            break
    return result


sample_numbers = [5, 1, 4, 2, 8]
print("\n29. Bubble sort result:", bubble_sort(sample_numbers))
print("    Original list stays unchanged:", sample_numbers)

# Example 30: Make sorting reusable with a function.
# A key and reverse option let the same helper sort different kinds of values.
def sort_values(values, key=None, reverse=False):
    """Return a sorted copy, optionally using a key and reverse order."""
    return sorted(values, key=key, reverse=reverse)


print("\n30. Reusable sorting function:")
print("    Numbers:", sort_values([4, 1, 3, 2]))
print("    Words by length:", sort_values(["elephant", "cat", "dog"], key=len))
print("    Descending:", sort_values([4, 1, 3, 2], reverse=True))
