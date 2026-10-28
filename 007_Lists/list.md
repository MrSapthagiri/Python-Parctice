# Module 7: Python Lists

Lists are one of Python's most useful data structures. They keep items in order,
allow duplicates, and can be changed after they are created. This module moves
from the fundamentals to practical list-based data processing.

## Learning goals

By the end of this module, you should be able to:

- Create lists and choose suitable values for them.
- Read, update, and process list items.
- Use common list methods and list comprehensions.
- Represent grouped data with nested lists.
- Sort values using built-in and custom sorting keys.
- Search lists and choose an approach that fits the data.

## Core topics

These are the six main topics in this module. Each has a dedicated file with
definitions, syntax, a flowchart, runnable examples, and explanations.

| File | Topic | What you will practice |
|---|---|---|
| `01_list_basics.py` | List Basics | Create, access, update, loop through, and process list values with 30 examples |
| `02_list_methods.py` | List Methods | Add, remove, count, find, copy, and reorder list values |
| `03_nested_lists.py` | Nested Lists | Rows, tables, nested iteration, and avoiding shared-row bugs |
| `04_list_comprehensions.py` | List Comprehension | Transforming, filtering, and conditionally building lists |
| `05_sorting_lists.py` | Sorting | 30 examples from basic ordering through custom keys and a bubble-sort demonstration |
| `06_searching_lists.py` | Searching | Membership, `index()`, linear search, and binary search |

Every lesson is a standalone `.py` file. The Basics and Sorting lessons each
include 30 examples; all lessons explain the topic and demonstrate code.
The flowcharts describe decision or processing steps; they are not Python
syntax.

## How to study

1. Study the six topics in the order shown above.
2. Read the topic and syntax notes at the top of each file.
3. Run a lesson with Python from this folder, for example:

   ```text
   python 01_list_basics.py
   ```

4. Predict the output before running each example, then compare your result.
5. Try changing the sample data and observe which results change.
6. Re-run examples after changing their input values to check your understanding.

## Quick reference

```python
items = ["pen", "book", "pen"]  # Create an ordered, changeable list
items[0] = "pencil"             # Replace an item
items.append("ruler")           # Add one item at the end
items.extend(["tape", "glue"])  # Add multiple items
first_two = items[:2]           # Make a slice (a new list)
items.pop()                     # Remove and return the final item
ordered_items = sorted(items)   # Get a sorted copy
```

List indexes start at `0`. Lists are mutable, so an assignment such as
`items[0] = "pencil"` changes the existing list. A slice such as `items[:2]`
creates a new outer list. See `08_copying_lists.py` for what that means when
items inside the list are themselves mutable.
