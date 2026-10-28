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

Run this file to see all 30 examples. The lessons are grouped from EASY to
MEDIUM to HARD. Each example includes its expected output in a comment.
"""

print("=" * 60)
print("EASY: CREATE, READ, AND CHANGE LISTS")
print("=" * 60)

# Example 1: Create a list.
# A list literal uses square brackets, with values separated by commas.
fruits = ["apple", "banana", "orange"]
print("\n1. Create a list:", fruits)
# Output: 1. Create a list: ['apple', 'banana', 'orange']

# Example 2: Create an empty list.
# Start empty when the program will collect values later.
shopping_cart = []
print("\n2. Empty list:", shopping_cart)
# Output: 2. Empty list: []

# Example 3: Count list items.
# len() returns how many items the list contains.
colors = ["red", "green", "blue"]
print("\n3. Number of colors:", len(colors))
# Output: 3. Number of colors: 3

# Example 4: Lists can contain duplicate values.
# Each occurrence counts as a separate item.
visitors = ["Mina", "Noah", "Mina"]
print("\n4. Visitors:", visitors)
print("   Number of visitor entries:", len(visitors))
# Output:
# 4. Visitors: ['Mina', 'Noah', 'Mina']
#    Number of visitor entries: 3

# Example 5: Keep related values together.
# Lists can contain different types, although one consistent type is often
# easier to work with.
student = ["Asha", 16, True]
print("\n5. Student record:", student)
print(f"   Name: {student[0]}, age: {student[1]}, enrolled: {student[2]}")
# Output:
# 5. Student record: ['Asha', 16, True]
#    Name: Asha, age: 16, enrolled: True

# Example 6: Read an item by its position.
# Indexes start at zero, so index 1 means the second item.
animals = ["cat", "dog", "rabbit"]
print("\n6. Second animal:", animals[1])
# Output: 6. Second animal: dog

# Example 7: Read from the end with a negative index.
# Index -1 means the last item.
planets = ["Mercury", "Venus", "Earth", "Mars"]
print("\n7. Last planet in this list:", planets[-1])
# Output: 7. Last planet in this list: Mars

# Example 8: Get part of a list with slicing.
# The start is included and the stop is excluded.
letters = ["a", "b", "c", "d", "e"]
print("\n8. Items at indexes 1 through 3:", letters[1:4])
# Output: 8. Items at indexes 1 through 3: ['b', 'c', 'd']

# Example 9: Replace an item.
# Lists are mutable: assignment can change an existing item.
scores = [72, 81, 90]
scores[0] = 75
print("\n9. Updated scores:", scores)
# Output: 9. Updated scores: [75, 81, 90]

# Example 10: Add one item at the end.
# append() adds its argument as one item.
tasks = ["plan", "write"]
tasks.append("review")
print("\n10. Task list after append():", tasks)
# Output: 10. Task list after append(): ['plan', 'write', 'review']

print("\n" + "=" * 60)
print("MEDIUM: ADD, REMOVE, AND CHECK")
print("=" * 60)

# Example 11: Add several items.
# extend() adds each value from the given iterable to the list.
tools = ["editor", "terminal"]
tools.extend(["browser", "debugger"])
print("\n11. Tools after extend():", tools)
# Output: 11. Tools after extend(): ['editor', 'terminal', 'browser', 'debugger']

# Example 12: Insert an item at a chosen position.
# insert(index, value) shifts later items to make room.
queue = ["second", "third"]
queue.insert(0, "first")
print("\n12. Queue after insert():", queue)
# Output: 12. Queue after insert(): ['first', 'second', 'third']

# Example 13: Remove an item by value safely.
# remove() deletes the first match; check membership to avoid ValueError.
colors = ["red", "green", "blue"]
color_to_remove = "green"
if color_to_remove in colors:
    colors.remove(color_to_remove)
print("\n13. Colors after removing green:", colors)
# Output: 13. Colors after removing green: ['red', 'blue']

# Example 14: Remove and use the last item.
# pop() returns the removed item, which is useful for a stack.
undo_stack = ["typed title", "added paragraph", "changed font"]
last_action = undo_stack.pop()
print("\n14. Undid:", last_action)
print("    Remaining actions:", undo_stack)
# Output:
# 14. Undid: changed font
#     Remaining actions: ['typed title', 'added paragraph']

# Example 15: Remove an item by its position.
# del removes the item at the specified index.
days = ["Monday", "Tuesday", "Wrong day", "Wednesday"]
del days[2]
print("\n15. Corrected days:", days)
# Output: 15. Corrected days: ['Monday', 'Tuesday', 'Wednesday']

# Example 16: Check whether an item exists.
# The in operator returns True or False.
allowed_users = ["Ari", "Bea", "Chen"]
print("\n16. Is Bea allowed?", "Bea" in allowed_users)
print("    Is Drew allowed?", "Drew" in allowed_users)
# Output:
# 16. Is Bea allowed? True
#     Is Drew allowed? False

# Example 17: Count how often a value appears.
# count() is helpful when duplicates are meaningful.
votes = ["yes", "no", "yes", "yes", "no"]
print("\n17. Yes votes:", votes.count("yes"))
# Output: 17. Yes votes: 3

# Example 18: Loop through each item.
# A for loop is a clear way to process every value.
books = ["Dune", "Matilda", "Coraline"]
print("\n18. Books:")
for book in books:
    print("   -", book)
# Output:
# 18. Books:
#    - Dune
#    - Matilda
#    - Coraline

# Example 19: Show each item's position with enumerate().
# start=1 makes the displayed positions friendlier for people.
names = ["Ari", "Bea", "Chen"]
print("\n19. Numbered names:")
for number, name in enumerate(names, start=1):
    print(f"   {number}. {name}")
# Output:
# 19. Numbered names:
#    1. Ari
#    2. Bea
#    3. Chen

# Example 20: Calculate a total and average.
# sum() adds numeric values; divide by len() to get their average.
temperatures = [18, 20, 22, 24]
average = sum(temperatures) / len(temperatures)
print(f"\n20. Average temperature: {average:.1f} C")
# Output: 20. Average temperature: 21.0 C

print("\n" + "=" * 60)
print("HARD: BUILD USEFUL RESULTS")
print("=" * 60)

# Example 21: Find the smallest and largest values.
# min() and max() work on a non-empty list of comparable values.
prices = [3.50, 1.25, 4.00, 2.75]
print("\n21. Lowest price:", min(prices))
print("    Highest price:", max(prices))
# Output:
# 21. Lowest price: 1.25
#     Highest price: 4.0

# Example 22: Filter values with a list comprehension.
# Keep only values that pass the condition after the if.
scores = [48, 76, 91, 55, 83]
passing_scores = [score for score in scores if score >= 60]
print("\n22. Passing scores:", passing_scores)
# Output: 22. Passing scores: [76, 91, 83]

# Example 23: Transform every value with a list comprehension.
# The expression before for describes each new value.
numbers = [2, 4, 6, 8]
doubled = [number * 2 for number in numbers]
print("\n23. Doubled numbers:", doubled)
# Output: 23. Doubled numbers: [4, 8, 12, 16]

# Example 24: Sort values and keep the original list unchanged.
# sorted() returns a new sorted list.
original_scores = [82, 65, 91, 73]
ordered_scores = sorted(original_scores)
print("\n24. Original order:", original_scores)
print("    Sorted order:", ordered_scores)
# Output:
# 24. Original order: [82, 65, 91, 73]
#     Sorted order: [65, 73, 82, 91]

# Example 25: Sort words by their length.
# key=len tells sorted() to compare each word's length.
words = ["elephant", "cat", "giraffe", "dog"]
words_by_length = sorted(words, key=len)
print("\n25. Words from shortest to longest:", words_by_length)
# Output: 25. Words from shortest to longest: ['cat', 'dog', 'giraffe', 'elephant']

# Example 26: Search for a value and safely get its position.
# index() raises ValueError when no match exists, so check with in first.
team = ["Ari", "Bea", "Chen"]
target = "Bea"
if target in team:
    print(f"\n26. {target} is at index {team.index(target)}.")
else:
    print(f"\n26. {target} is not in the team.")
# Output: 26. Bea is at index 1.

print("\n" + "=" * 60)
print("HARD: COMBINE LIST SKILLS")
print("=" * 60)

# Example 27: Read values from a nested list.
# The first index selects a row; the second index selects a value in that row.
seats = [
    ["A1", "A2", "A3"],
    ["B1", "B2", "B3"],
]
print("\n27. Seat in row 2, column 3:", seats[1][2])
# Output: 27. Seat in row 2, column 3: B3

# Example 28: Copy a list before changing it.
# copy() makes a separate outer list, so adding here does not change fruits.
fruits = ["apple", "banana"]
more_fruits = fruits.copy()
more_fruits.append("orange")
print("\n28. Original fruits:", fruits)
print("    Copied and updated:", more_fruits)
# Output:
# 28. Original fruits: ['apple', 'banana']
#     Copied and updated: ['apple', 'banana', 'orange']

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
# Output: 29. Unique tags in order: ['python', 'beginner', 'lists']

# Example 30: Split a list into smaller groups.
# range() chooses each group start; slicing safely handles the final short group.
all_scores = [88, 91, 76, 84, 95, 79, 87]
group_size = 3
score_groups = [
    all_scores[start : start + group_size]
    for start in range(0, len(all_scores), group_size)
]
print("\n30. Scores in groups of three:", score_groups)
# Output: 30. Scores in groups of three: [[88, 91, 76], [84, 95, 79], [87]]
