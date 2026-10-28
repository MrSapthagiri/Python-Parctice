"""
MODULE 7.10: SORTING LISTS

DEFINITION
Sorting arranges list items into an order. Use list.sort() to reorder a list
in place, or sorted(iterable) to create and return a new sorted list.

SYNTAX
    values.sort()
    values.sort(reverse=True)
    values.sort(key=some_function)
    ordered = sorted(values)
    ordered = sorted(values, key=some_function, reverse=True)

IMPORTANT
- sort() changes the original list and returns None.
- sorted() returns a new list and leaves the input order unchanged.
- key= tells Python which value to compare, such as len or a dictionary field.
- Python sorting is stable: equal keys keep their original relative order.
- Values must be mutually comparable; sort numbers separately from strings.

FLOWCHART: CHOOSE HOW TO SORT
    [Need an ordered result?]
       |
       v
    [Keep original order unchanged?]
       | Yes                         | No
       v                             v
    [Use sorted()]              [Use list.sort()]
       |                             |
       +--------------+--------------+
                      |
                      v
             [Need custom ordering?]
                      |
                 Yes  v
                 [Set key=...]
                      |
                      v
             [Need descending order?]
                      |
                 Yes  v
             [Set reverse=True]
"""

print("Example 1: Sort numbers without changing the source")
scores = [82, 65, 91, 73]
ascending_scores = sorted(scores)
print(f"Original: {scores}")
print(f"Sorted:   {ascending_scores}")

print("\nExample 2: Sort in descending order")
descending_scores = sorted(scores, reverse=True)
print(descending_scores)

print("\nExample 3: sort() changes a list in place")
tasks = ["write", "plan", "review"]
result = tasks.sort()
print(tasks)   # ['plan', 'review', 'write']
print(result)  # None

print("\nExample 4: Sort words by length")
words = ["comprehension", "loop", "list", "function"]
words.sort(key=len)
print(words)

print("\nExample 5: Sort strings without case affecting order")
names = ["zoe", "Ari", "maya", "Bea"]
print(sorted(names, key=str.casefold))

print("\nExample 6: Sort records by a selected field")
products = [
    {"name": "Notebook", "price": 3.50},
    {"name": "Pencil", "price": 0.80},
    {"name": "Folder", "price": 2.25},
]
by_price = sorted(products, key=lambda product: product["price"])
for product in by_price:
    print(f"{product['name']}: ${product['price']:.2f}")

print("\nExample 7: Stable sorting")
students = [("Ari", 90), ("Bea", 82), ("Chen", 90)]
by_score = sorted(students, key=lambda student: student[1], reverse=True)
print(by_score)  # Ari remains before Chen because their scores are equal.

# Use sorted() if another part of the program still needs the original order.
