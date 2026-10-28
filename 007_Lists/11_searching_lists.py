"""
SEARCHING LISTS

DEFINITION
Searching checks whether a value is present and may find its position.
Membership testing with "in" is concise; index() returns the first matching
position but raises ValueError when no match exists.

SYNTAX
    found = target in values
    position = values.index(target)
    position = values.index(target, start, stop)

SEARCH APPROACHES
- Membership / index(): simple built-in search; linear time for a list.
- Linear search: inspect items one by one; works on unsorted lists.
- Binary search: repeatedly halve the search range; requires sorted data.
- For repeated searches in a large collection, a set or dictionary may be
  more suitable than repeatedly scanning a list.

FLOWCHART: LINEAR SEARCH
    [Start at first item]
       |
       v
    [More items?] -- No --> [Not found]
       |
      Yes
       |
       v
    [Does item match target?] -- Yes --> [Return its index]
       |
       No
       |
       +---------------------> [Check next item]

FLOWCHART: BINARY SEARCH (SORTED LIST ONLY)
    [Set low and high bounds]
       |
       v
    [low <= high?] -- No --> [Not found]
       |
      Yes
       |
       v
    [Check middle item]
       |
       +--> [Equal?] --> Yes --> [Found]
       |
       +--> [Target smaller?] --> Yes --> [Move high left]
       |
       +--> [Target larger?] --> Yes --> [Move low right]
       |
       +-------------------------------> [Repeat]
"""


def linear_search(values: list[int], target: int) -> int:
    """Return the first matching index, or -1 if the target is absent."""
    for index, value in enumerate(values):
        if value == target:
            return index
    return -1


def binary_search(sorted_values: list[int], target: int) -> int:
    """Return a matching index in an ascending list, or -1 if absent."""
    low = 0
    high = len(sorted_values) - 1

    while low <= high:
        middle = (low + high) // 2
        value = sorted_values[middle]

        if value == target:
            return middle
        if value < target:
            low = middle + 1
        else:
            high = middle - 1

    return -1


print("Example 1: Membership test")
colors = ["red", "green", "blue"]
print("green" in colors)   # True
print("orange" in colors)  # False

print("\nExample 2: Find a position safely")
if "blue" in colors:
    print(f"blue is at index {colors.index('blue')}")

print("\nExample 3: Guard index() when the value may be absent")
target_color = "orange"
if target_color in colors:
    print(colors.index(target_color))
else:
    print(f"{target_color} is not in the list.")

print("\nExample 4: Search a specific range with index()")
letters = ["a", "b", "c", "b", "d"]
print(letters.index("b", 2))  # Search from index 2; result is 3.

print("\nExample 5: Linear search works on unsorted lists")
unsorted_values = [42, 17, 91, 23]
print(linear_search(unsorted_values, 91))  # 2
print(linear_search(unsorted_values, 5))   # -1

print("\nExample 6: Binary search on ascending sorted data")
ordered_values = [3, 8, 12, 19, 27, 35, 44]
print(binary_search(ordered_values, 27))  # 4
print(binary_search(ordered_values, 20))  # -1

# Binary search is incorrect if its input list is not sorted ascending.
