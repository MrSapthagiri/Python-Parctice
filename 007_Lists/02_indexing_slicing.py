
MODULE 7.2: INDEXING AND SLICING

DEFINITION
Indexing reads one item by position. Slicing reads a range and returns a new
list. Positive indexes count from the start; negative indexes count from the end.

SYNTAX
    item = values[index]
    part = values[start:stop:step]

SLICE RULES
- The start position is included.
- The stop position is excluded.
- An omitted start, stop, or step uses its default.
- An index outside the list raises IndexError; it is not silently ignored.

FLOWCHART: GET A VALUE
    [Start with a list]
       |
       v
    [Need one item?] -- Yes --> [Use one index]
       |
       No
       |
       v
    [Need a range?]
       |
       v
    [Use start:stop:step]
       |
       v
    [Use the returned value or slice]
"""

letters = ["a", "b", "c", "d", "e", "f"]

print("Example 1: Positive indexes")
print(letters[0])  # a: first item
print(letters[2])  # c: third item

print("\nExample 2: Negative indexes")
print(letters[-1])  # f: last item
print(letters[-2])  # e: second item from the end

print("\nExample 3: A slice has an exclusive stop")
print(letters[1:4])  # ['b', 'c', 'd']

print("\nExample 4: Omitted boundaries")
print(letters[:3])   # First three items
print(letters[3:])   # From index 3 to the end
print(letters[:])    # A shallow copy of the outer list

print("\nExample 5: Step through a list")
print(letters[::2])   # Every second item: ['a', 'c', 'e']
print(letters[::-1])  # A reversed copy: ['f', 'e', 'd', 'c', 'b', 'a']

print("\nExample 6: Safe index validation")
requested_index = 10
if 0 <= requested_index < len(letters):
    print(letters[requested_index])
else:
    print(f"Index {requested_index} is outside the list.")

# A slice creates a new outer list; see 08_copying_lists.py for nested values.
