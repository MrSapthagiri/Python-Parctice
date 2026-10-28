"""
MODULE 7.1: LIST BASICS - 30 PRACTICAL EXAMPLES

WHAT IS A LIST?
A list is an ordered, changeable collection of values. Lists use square
brackets, allow duplicate values, and can grow or shrink while a program runs.

SYNTAX
    names = ["Asha", "Ben", "Chen"]
    first_name = names[0]
    names.append("Dina")

FLOWCHART
    [Create a list]
          |
          v
    [Read or update items]
          |
          v
    [Add, remove, search, or process items]
          |
          v
    [Use the result]

Run this file to see all 30 examples. Each example is independent and builds
from simple list operations toward small, practical data-processing tasks.
"""

print("=" * 60)
print("BEGINNER: CREATE, READ, AND CHANGE LISTS")
print("=" * 60)

# Example 1: Create a list.
# A list literal uses square brackets, with values separated by commas.
fruits = ["apple", "banana", "orange"]
print("\n1. Create a list:", fruits)

# Example 2: Create an empty list.
# Start empty when the program will collect values later.
shopping_cart = []
print("\n2. Empty list:", shopping_cart)

# Example 3: Count list items.
# len() returns how many items the list contains.
colors = ["red", "green", "blue"]
print("\n3. Number of colors:", len(colors))

# Example 4: Lists can contain duplicate values.
# Each occurrence counts as a separate item.
visitors = ["Mina", "Noah", "Mina"]
print("\n4. Visitors:", visitors)
print("   Number of visitor entries:", len(visitors))

# Example 5: Keep related values together.
# Lists can contain different types, although one consistent type is often
# easier to work with.
student = ["Asha", 16, True]
print("\n5. Student record:", student)
print(f"   Name: {student[0]}, age: {student[1]}, enrolled: {student[2]}")

# Example 6: Read an item by its position.
# Indexes start at zero, so index 1 means the second item.
animals = ["cat", "dog", "rabbit"]
print("\n6. Second animal:", animals[1])

# Example 7: Read from the end with a negative index.
# Index -1 means the last item.
planets = ["Mercury", "Venus", "Earth", "Mars"]
print("\n7. Last planet in this list:", planets[-1])

# Example 8: Get part of a list with slicing.
# The start is included and the stop is excluded.
letters = ["a", "b", "c", "d", "e"]
print("\n8. Items at indexes 1 through 3:", letters[1:4])

# Example 9: Replace an item.
# Lists are mutable: assignment can change an existing item.
scores = [72, 81, 90]
scores[0] = 75
print("\n9. Updated scores:", scores)

# Example 10: Add one item at the end.
# append() adds its argument as one item.
tasks = ["plan", "write"]
tasks.append("review")
print("\n10. Task list after append():", tasks)

print("\n" + "=" * 60)
print("BEGINNER TO INTERMEDIATE: ADD, REMOVE, AND CHECK")
print("=" * 60)

# Example 11: Add several items.
# extend() adds each value from the given iterable to the list.
tools = ["editor", "terminal"]
tools.extend(["browser", "debugger"])
print("\n11. Tools after extend():", tools)

# Example 12: Insert an item at a chosen position.
# insert(index, value) shifts later items to make room.
queue = ["second", "third"]
queue.insert(0, "first")
print("\n12. Queue after insert():", queue)

# Example 13: Remove an item by value safely.
# remove() deletes the first match; check membership to avoid ValueError.
colors = ["red", "green", "blue"]
color_to_remove = "green"
if color_to_remove in colors:
    colors.remove(color_to_remove)
print("\n13. Colors after removing green:", colors)

# Example 14: Remove and use the last item.
# pop() returns the removed item, which is useful for a stack.
undo_stack = ["typed title", "added paragraph", "changed font"]
last_action = undo_stack.pop()
print("\n14. Undid:", last_action)
print("    Remaining actions:", undo_stack)

# Example 15: Remove an item by its position.
# del removes the item at the specified index.
days = ["Monday", "Tuesday", "Wrong day", "Wednesday"]
del days[2]
print("\n15. Corrected days:", days)

# Example 16: Check whether an item exists.
# The in operator returns True or False.
allowed_users = ["Ari", "Bea", "Chen"]
print("\n16. Is Bea allowed?", "Bea" in allowed_users)
print("    Is Drew allowed?", "Drew" in allowed_users)

# Example 17: Count how often a value appears.
# count() is helpful when duplicates are meaningful.
votes = ["yes", "no", "yes", "yes", "no"]
print("\n17. Yes votes:", votes.count("yes"))

# Example 18: Loop through each item.
# A for loop is a clear way to process every value.
books = ["Dune", "Matilda", "Coraline"]
print("\n18. Books:")
for book in books:
    print("   -", book)

# Example 19: Show each item's position with enumerate().
# start=1 makes the displayed positions friendlier for people.
names = ["Ari", "Bea", "Chen"]
print("\n19. Numbered names:")
for number, name in enumerate(names, start=1):
    print(f"   {number}. {name}")

# Example 20: Calculate a total and average.
# sum() adds numeric values; divide by len() to get their average.
temperatures = [18, 20, 22, 24]
average = sum(temperatures) / len(temperatures)
print(f"\n20. Average temperature: {average:.1f} C")

print("\n" + "=" * 60)
print("INTERMEDIATE: BUILD USEFUL RESULTS")
print("=" * 60)

# Example 21: Find the smallest and largest values.
# min() and max() work on a non-empty list of comparable values.
prices = [3.50, 1.25, 4.00, 2.75]
print("\n21. Lowest price:", min(prices))
print("    Highest price:", max(prices))

# Example 22: Filter values with a list comprehension.
# Keep only values that pass the condition after the if.
scores = [48, 76, 91, 55, 83]
passing_scores = [score for score in scores if score >= 60]
print("\n22. Passing scores:", passing_scores)

# Example 23: Transform every value with a list comprehension.
# The expression before for describes each new value.
numbers = [2, 4, 6, 8]
doubled = [number * 2 for number in numbers]
print("\n23. Doubled numbers:", doubled)

# Example 24: Sort values and keep the original list unchanged.
# sorted() returns a new sorted list.
original_scores = [82, 65, 91, 73]
ordered_scores = sorted(original_scores)
print("\n24. Original order:", original_scores)
print("    Sorted order:", ordered_scores)

# Example 25: Sort words by their length.
# key=len tells sorted() to compare each word's length.
words = ["elephant", "cat", "giraffe", "dog"]
words_by_length = sorted(words, key=len)
print("\n25. Words from shortest to longest:", words_by_length)

# Example 26: Search for a value and safely get its position.
# index() raises ValueError when no match exists, so check with in first.
team = ["Ari", "Bea", "Chen"]
target = "Bea"
if target in team:
    print(f"\n26. {target} is at index {team.index(target)}.")
else:
    print(f"\n26. {target} is not in the team.")

print("\n" + "=" * 60)
print("HIGHER LEVEL: COMBINE LIST SKILLS")
print("=" * 60)

# Example 27: Read values from a nested list.
# The first index selects a row; the second index selects a value in that row.
seats = [
    ["A1", "A2", "A3"],
    ["B1", "B2", "B3"],
]
print("\n27. Seat in row 2, column 3:", seats[1][2])

# Example 28: Copy a list before changing it.
# copy() makes a separate outer list, so adding here does not change fruits.
fruits = ["apple", "banana"]
more_fruits = fruits.copy()
more_fruits.append("orange")
print("\n28. Original fruits:", fruits)
print("    Copied and updated:", more_fruits)

# Example 29: Remove duplicates while keeping their first-seen order.
# A set tracks what was seen; the result list preserves the original order.
raw_tags = ["python", "beginner", "python", "lists", "beginner"]
unique_tags = []
seen_tags = set()
for tag in raw_tags:
    if tag not in seen_tags:
        unique_tags.append(tag)
        seen_tags.add(tag)
print("\n29. Unique tags in order:", unique_tags)

# Example 30: Split a list into smaller groups.
# range() chooses each group start; slicing safely handles the final short group.
all_scores = [88, 91, 76, 84, 95, 79, 87]
group_size = 3
score_groups = [
    all_scores[start : start + group_size]
    for start in range(0, len(all_scores), group_size)
]
print("\n30. Scores in groups of three:", score_groups)
