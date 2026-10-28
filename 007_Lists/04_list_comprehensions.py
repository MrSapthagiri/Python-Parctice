"""
MODULE 7.6: LIST COMPREHENSIONS

DEFINITION
A list comprehension creates a new list from an iterable in one expression.
It is a concise alternative to a simple loop that appends results to a list.

SYNTAX
    [expression for item in iterable]
    [expression for item in iterable if condition]
    [value_if_true if condition else value_if_false for item in iterable]

READ IT IN THIS ORDER
    expression <- for item in iterable <- optional if condition

FLOWCHART: BUILD A RESULT LIST
    [Start with source items]
       |
       v
    [Get next item]
       |
       v
    [Does it pass the optional condition?]
       | Yes                        | No
       v                            +------> [Skip item]
    [Calculate expression]
       |
       v
    [Append result to new list]
       |
       +----------------------------> [More items?]

Use a regular loop when it makes the logic easier to understand, especially
when the expression has multiple steps or side effects.
"""

print("Example 1: Transform every value")
numbers = [1, 2, 3, 4]
squares = [number**2 for number in numbers]
print(squares)

print("\nExample 2: Filter values")
values = [3, 8, 11, 14, 17, 20]
even_values = [value for value in values if value % 2 == 0]
print(even_values)

print("\nExample 3: Transform and filter")
prices = [12.0, 25.0, 8.0, 40.0]
discounted = [round(price * 0.9, 2) for price in prices if price >= 10]
print(discounted)

print("\nExample 4: Use an if/else expression")
scores = [45, 70, 88]
labels = ["pass" if score >= 60 else "retry" for score in scores]
print(labels)

print("\nExample 5: Normalize text")
raw_names = ["  ADA ", "Grace", "  Linus"]
clean_names = [name.strip().title() for name in raw_names]
print(clean_names)

print("\nExample 6: Equivalent loop for clarity")
source = [2, 5, 8, 11]
tripled_odds = []
for value in source:
    if value % 2 == 1:
        tripled_odds.append(value * 3)
print(tripled_odds)

# Avoid deeply nested comprehensions; split complex steps into named variables.
