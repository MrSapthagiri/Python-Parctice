"""
NESTED LISTS

DEFINITION
A nested list is a list that contains other lists. It can represent a small
table, grid, or grouped data. The outer index chooses a row; the inner index
chooses a value within that row.

SYNTAX
    table = [
        ["Name", "Score"],
        ["Ari", 91],
    ]
    value = table[row_index][column_index]
    for row in table:
        for value in row:
            ...

FLOWCHART: READ A TABLE CELL
    [Start with rows]
       |
       v
    [Choose outer index (row)]
       |
       v
    [Choose inner index (column)]
       |
       v
    [Read or update the cell]

For regular rectangular data, every row should have the same number of
columns. A nested list is not the same as a two-dimensional array library.
"""

print("Example 1: Read a cell")
students = [
    ["Ari", 91, 88],
    ["Bea", 78, 84],
    ["Chen", 95, 92],
]
print(students[0][0])  # Ari
print(students[1][2])  # 84

print("\nExample 2: Visit every value")
for row in students:
    for value in row:
        print(value, end=" | ")
    print()

print("\nExample 3: Calculate a total for each row")
for row in students:
    name = row[0]
    scores = row[1:]
    average = sum(scores) / len(scores)
    print(f"{name}: average {average:.1f}")

print("\nExample 4: Update one cell")
students[1][1] = 80
print(students[1])

print("\nExample 5: Create a grid without shared rows")
grid = [[0 for _column in range(3)] for _row in range(2)]
grid[0][1] = 7
print(grid)  # [[0, 7, 0], [0, 0, 0]]

print("\nExample 6: A common shared-row mistake")
shared_rows = [[0] * 3] * 2
shared_rows[0][0] = 9
print(shared_rows)  # Both rows changed because they refer to one inner list.

# Prefer the comprehension in Example 5 when creating independent rows.
