"""
MODULE 7.8: COPYING LISTS AND MUTABILITY

DEFINITION
Assignment does not copy a list; it creates another reference to the same list.
A shallow copy creates a new outer list but keeps references to nested objects.
Use copy.deepcopy() when an independent copy of nested mutable data is required.

SYNTAX
    alias = original
    shallow = original.copy()
    shallow = original[:]
    from copy import deepcopy
    independent = deepcopy(original)

FLOWCHART: CHOOSE HOW TO COPY
    [Need another name for the same list?] -- Yes --> [Assignment / alias]
       |
       No
       |
       v
    [Does the list contain mutable nested values?]
       | No                          | Yes
       v                             v
    [copy() or slicing]       [Need nested values independent?]
                                      | Yes
                                      v
                               [deepcopy()]

Shallow copying and deep copying are different. Choose based on whether
mutations to nested objects must be isolated.
"""

print("Example 1: Assignment creates an alias")
original = ["draft", "review"]
alias = original
alias.append("publish")
print(original)  # The original changed too.
print(alias)

print("\nExample 2: copy() creates a separate outer list")
original = ["draft", "review"]
copied = original.copy()
copied.append("publish")
print(original)
print(copied)

print("\nExample 3: Slicing also shallow-copies the outer list")
original = [10, 20, 30]
copied = original[:]
copied[0] = 99
print(original)
print(copied)

print("\nExample 4: A shallow copy shares nested lists")
original = [["red", "blue"], ["circle", "square"]]
shallow = original.copy()
shallow[0].append("green")
print(original)  # The nested first list changed in both structures.
print(shallow)

print("\nExample 5: Deep-copy nested mutable values")
from copy import deepcopy

original = [["red", "blue"], ["circle", "square"]]
independent = deepcopy(original)
independent[0].append("green")
print(original)
print(independent)

# Use deepcopy only when you need independent nested mutable objects.
