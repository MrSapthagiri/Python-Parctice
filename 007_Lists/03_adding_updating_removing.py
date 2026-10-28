"""
MODULE 7.3: ADDING, UPDATING, AND REMOVING ITEMS

DEFINITION
Lists are mutable: you can replace an item, add items, or remove items after
creation. Pick an operation based on whether you have one item, many items, or
an item position.

SYNTAX
    values[index] = replacement
    values.append(item)          # one item at the end
    values.extend(iterable)      # each item from an iterable
    values.insert(index, item)   # one item at a position
    values.remove(item)          # first matching value
    removed = values.pop(index)  # item at index; default is last item
    del values[index]

FLOWCHART: CHOOSE AN OPERATION
    [Need to change a list?]
       |
       +--> [Replace a known position] --> [index assignment]
       |
       +--> [Add one item] -------------> [append() or insert()]
       |
       +--> [Add many items] ------------> [extend()]
       |
       +--> [Remove by value] ------------> [Check, then remove()]
       |
       +--> [Remove by position] ---------> [pop() or del]

IMPORTANT
- remove(value) raises ValueError when the value is absent.
- pop(index) raises IndexError when the position is invalid.
- append(list) adds that list as one nested item; extend(list) adds its items.
"""

print("Example 1: Replace an item")
tasks = ["plan", "review", "publish"]
tasks[1] = "test"
print(tasks)

print("\nExample 2: append() adds one item")
tasks.append("monitor")
print(tasks)

print("\nExample 3: extend() adds each item")
tasks.extend(["document", "archive"])
print(tasks)

print("\nExample 4: insert() adds at a position")
tasks.insert(1, "design")
print(tasks)

print("\nExample 5: remove by value after checking")
if "archive" in tasks:
    tasks.remove("archive")
print(tasks)

print("\nExample 6: pop() removes and returns an item")
last_task = tasks.pop()
print(f"Removed: {last_task}")
print(f"Remaining: {tasks}")

print("\nExample 7: del removes by position")
del tasks[0]
print(tasks)

print("\nExample 8: clear() removes all items")
temporary_queue = ["job-101", "job-102"]
temporary_queue.clear()
print(temporary_queue)

print("\nappend() compared with extend()")
one_nested_item = ["north", "south"]
one_nested_item.append(["east", "west"])
many_items = ["north", "south"]
many_items.extend(["east", "west"])
print(one_nested_item)  # The added list is a single nested item.
print(many_items)       # The added values are separate items.
