# Module 7: Python Lists

Lists are one of Python's most useful data structures. They keep items in order,
allow duplicates, and can be changed after they are created. This module moves
from the fundamentals to practical list-based data processing.

## Learning goals

By the end of this module, you should be able to:

- Create lists and choose suitable values for them.
- Read and update items with indexes and slices.
- Add, replace, and remove items safely.
- Select the right built-in list method.
- Iterate through lists and build useful results.
- Use list comprehensions for simple transformations and filters.
- Represent rows and records with nested lists.
- Avoid accidental shared changes when copying lists.
- Combine these skills in a small inventory-report example.

## Core topics

These are the six main topics in this module. Each has a dedicated file with
definitions, syntax, a flowchart, runnable examples, and explanations.

| File | Topic | What you will practice |
|---|---|---|
| `01_list_basics.py` | List Basics | Creating lists, order, indexes, mutability, and common operations |
| `04_list_methods.py` | List Methods | Add, remove, count, find, copy, and reorder list values |
| `07_nested_lists.py` | Nested Lists | Rows, tables, nested iteration, and avoiding shared-row bugs |
| `06_list_comprehensions.py` | List Comprehension | Transforming, filtering, and conditionally building lists |
| `10_sorting_lists.py` | Sorting | In-place `sort()`, `sorted()`, keys, reverse order, and stable sorting |
| `11_searching_lists.py` | Searching | Membership, `index()`, linear search, and binary search |

## Supporting lessons

Use these lessons to explore related list skills and practice the core topics:

| File | Topic | What you will practice |
|---|---|---|
| `02_indexing_slicing.py` | Indexing and slicing | Positive and negative indexes, slices, and steps |
| `03_adding_updating_removing.py` | Updating lists | Assignment, `append()`, `extend()`, `insert()`, `remove()`, `pop()`, and `del` |
| `05_looping_lists.py` | Looping through lists | `for`, `enumerate()`, filtering, totals, and searching |
| `08_copying_lists.py` | Copying safely | Aliasing, shallow copies, and nested mutable values |
| `09_inventory_project.py` | Practical mini-project | Validate product data, calculate stock value, and build a report |

Every lesson is a standalone `.py` file. Each file includes a definition,
syntax, a text flowchart, runnable examples, explanations, and practical
warnings or review points. The flowcharts describe the decision or processing
steps; they are not Python syntax.

## How to study

1. Study the six core topics in the order shown above.
2. Read the topic and syntax notes at the top of each file.
3. Run a lesson with Python from this folder, for example:

   ```text
   python 01_list_basics.py
   ```

4. Predict the output before running each example, then compare your result.
5. Try changing the sample data and observe which results change.
6. Finish by running `09_inventory_project.py` and tracing each helper function.

## Quick reference

```python
items = ["pen", "book", "pen"]  # Create an ordered, changeable list
items[0] = "pencil"             # Replace an item
items.append("ruler")           # Add one item at the end
items.extend(["tape", "glue"])  # Add multiple items
first_two = items[:2]           # Make a slice (a new list)
items.pop()                     # Remove and return the final item
```

List indexes start at `0`. Lists are mutable, so an assignment such as
`items[0] = "pencil"` changes the existing list. A slice such as `items[:2]`
creates a new outer list. See `08_copying_lists.py` for what that means when
items inside the list are themselves mutable.
