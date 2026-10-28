"""
MODULE 7.4: BUILT-IN LIST METHODS AND FUNCTIONS

DEFINITION
List methods perform common operations on a list. Some modify the list and
return None; others return information or a new list. Built-in functions such
as sorted() and len() work with lists but are not list methods.

SYNTAX
    values.append(item)
    values.count(item)
    values.index(item)
    values.sort()
    ordered = sorted(values)
    copied = values.copy()

METHOD QUICK GUIDE
    append, extend, insert  -> add items
    remove, pop, clear       -> remove items
    count, index             -> look up items
    sort, reverse            -> reorder the list in place
    copy                     -> shallow-copy the outer list

FLOWCHART: SELECT A TOOL
    [What result do you need?]
       |
       +--> [Add/remove] ------> [Use a mutation method]
       +--> [Count/find] ------> [Use count()/index()/in]
       +--> [Reorder in place] -> [Use sort()/reverse()]
       +--> [Keep original] ---> [Use sorted() or copy()]
"""

print("Example 1: count() and index()")
languages = ["Python", "Go", "Python", "Rust"]
print(languages.count("Python"))  # 2
if "Rust" in languages:
    print(languages.index("Rust"))  # 3

print("\nExample 2: sort() changes the original list")
scores = [84, 61, 93, 75]
result = scores.sort()
print(scores)  # [61, 75, 84, 93]
print(result)  # None: sort() modifies in place.

print("\nExample 3: sorted() returns a new ordered list")
original = [84, 61, 93, 75]
ascending = sorted(original)
descending = sorted(original, reverse=True)
print(original)
print(ascending)
print(descending)

print("\nExample 4: sort strings by length")
words = ["python", "is", "useful"]
words.sort(key=len)
print(words)  # ['is', 'python', 'useful']

print("\nExample 5: reverse() changes the original list")
queue = ["first", "second", "third"]
queue.reverse()
print(queue)

print("\nExample 6: count before indexing")
colors = ["blue", "green", "blue"]
target = "orange"
if target in colors:
    print(colors.index(target))
else:
    print(f"{target} is not in the list.")

print("\nExample 7: len(), min(), max(), and sum()")
measurements = [12, 8, 15, 10]
print(f"Count: {len(measurements)}")
print(f"Minimum: {min(measurements)}")
print(f"Maximum: {max(measurements)}")
print(f"Total: {sum(measurements)}")

# Do not assign values.sort() to a variable expecting the sorted list.
