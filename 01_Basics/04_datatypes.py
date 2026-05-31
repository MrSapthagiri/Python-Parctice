# 04_datatypes.py



print("==========================================")
print("PYTHON DATA TYPES - BY DIFFICULTY LEVEL")
print("==========================================")

# ==========================================
# LOW LEVEL DATA TYPES (Beginner Level)
# ==========================================
print("\n" + "="*50)
print("LOW LEVEL DATA TYPES (Beginner - Most Common)")
print("="*50)

# 1. Integer (int) - Whole numbers
print("\n1. INTEGER (int)")
print("-" * 20)
age = 25
negative_num = -10
zero = 0
large_num = 1000000
print(f"Age: {age}, type: {type(age)}")
print(f"Negative: {negative_num}, type: {type(negative_num)}")
print(f"Zero: {zero}, type: {type(zero)}")
print(f"Large number: {large_num}, type: {type(large_num)}")

# 2. Float (float) - Decimal numbers
print("\n2. FLOAT (float)")
print("-" * 20)
height = 5.9
pi = 3.14159
negative_float = -2.5
scientific = 1.23e-4
print(f"Height: {height}, type: {type(height)}")
print(f"Pi: {pi}, type: {type(pi)}")
print(f"Negative float: {negative_float}, type: {type(negative_float)}")
print(f"Scientific notation: {scientific}, type: {type(scientific)}")

# 3. String (str) - Text data
print("\n3. STRING (str)")
print("-" * 20)
name = "Alice"
message = 'Hello World!'
multiline = """This is a
multiline string"""
empty_string = ""
print(f"Name: {name}, type: {type(name)}")
print(f"Message: {message}, type: {type(message)}")
print(f"Multiline: {multiline!r}, type: {type(multiline)}")
print(f"Empty string: {empty_string!r}, type: {type(empty_string)}")

# 4. Boolean (bool) - True/False values
print("\n4. BOOLEAN (bool)")
print("-" * 20)
is_student = True
is_teacher = False
has_passed = True
is_active = False
print(f"Is student: {is_student}, type: {type(is_student)}")
print(f"Is teacher: {is_teacher}, type: {type(is_teacher)}")
print(f"Has passed: {has_passed}, type: {type(has_passed)}")
print(f"Is active: {is_active}, type: {type(is_active)}")

# 5. None Type (NoneType) - Represents absence of value
print("\n5. NONE TYPE (NoneType)")
print("-" * 20)
result = None
empty_variable = None
print(f"Result: {result}, type: {type(result)}")
print(f"Empty variable: {empty_variable}, type: {type(empty_variable)}")

print("\n" + "="*50)
print("LOW LEVEL SUMMARY")
print("="*50)
print("[OK] int - Whole numbers (positive, negative, zero)")
print("[OK] float - Decimal numbers")
print("[OK] str - Text/characters")
print("[OK] bool - True/False values")
print("[OK] NoneType - Represents 'nothing' or absence of value")
print("\nThese are the most fundamental data types you'll use daily!")

# ==========================================
# MEDIUM LEVEL DATA TYPES (Intermediate Level)
# ==========================================
print("\n\n" + "="*50)
print("MEDIUM LEVEL DATA TYPES (Intermediate - Collections)")
print("="*50)

# 1. List (list) - Mutable ordered collection
print("\n1. LIST (list) - Mutable Ordered Collection")
print("-" * 40)
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed_list = [1, "hello", True, 3.14]
empty_list = []
nested_list = [[1, 2], [3, 4], [5, 6]]
print(f"Fruits: {fruits}, type: {type(fruits)}")
print(f"Numbers: {numbers}, type: {type(numbers)}")
print(f"Mixed: {mixed_list}, type: {type(mixed_list)}")
print(f"Empty: {empty_list}, type: {type(empty_list)}")
print(f"Nested: {nested_list}, type: {type(nested_list)}")

# 2. Tuple (tuple) - Immutable ordered collection
print("\n2. TUPLE (tuple) - Immutable Ordered Collection")
print("-" * 40)
coordinates = (10, 20, 30)
rgb_colors = ("red", "green", "blue")
single_item = (42,)  # Note the comma!
empty_tuple = ()
nested_tuple = ((1, 2), (3, 4), (5, 6))
print(f"Coordinates: {coordinates}, type: {type(coordinates)}")
print(f"RGB Colors: {rgb_colors}, type: {type(rgb_colors)}")
print(f"Single item: {single_item}, type: {type(single_item)}")
print(f"Empty: {empty_tuple}, type: {type(empty_tuple)}")
print(f"Nested: {nested_tuple}, type: {type(nested_tuple)}")

# 3. Dictionary (dict) - Key-value pairs
print("\n3. DICTIONARY (dict) - Key-Value Pairs")
print("-" * 40)
person = {"name": "Bob", "age": 30, "city": "New York"}
student_grades = {"Alice": 95, "Bob": 87, "Charlie": 92}
empty_dict = {}
nested_dict = {"person": {"name": "Alice", "age": 25}, "scores": [85, 90, 88]}
print(f"Person info: {person}, type: {type(person)}")
print(f"Student grades: {student_grades}, type: {type(student_grades)}")
print(f"Empty: {empty_dict}, type: {type(empty_dict)}")
print(f"Nested: {nested_dict}, type: {type(nested_dict)}")

# 4. Set (set) - Unordered unique collection
print("\n4. SET (set) - Unordered Unique Collection")
print("-" * 40)
unique_numbers = {1, 2, 3, 4, 5}
unique_fruits = {"apple", "banana", "apple", "cherry"}  # Duplicates removed
empty_set = set()  # Note: {} creates dict, not set
from_list = set([1, 2, 2, 3, 3, 3])  # Remove duplicates from list
print(f"Unique numbers: {unique_numbers}, type: {type(unique_numbers)}")
print(f"Unique fruits: {unique_fruits}, type: {type(unique_fruits)}")
print(f"Empty set: {empty_set}, type: {type(empty_set)}")
print(f"From list: {from_list}, type: {type(from_list)}")

print("\n" + "="*50)
print("MEDIUM LEVEL SUMMARY")
print("="*50)
print("[OK] list - Mutable ordered collections (can change contents)")
print("[OK] tuple - Immutable ordered collections (cannot change contents)")
print("[OK] dict - Key-value pair collections (like a phone book)")
print("[OK] set - Unordered unique collections (no duplicates)")
print("\nThese handle collections of data and require understanding mutability!")

# ==========================================
# HIGH LEVEL DATA TYPES (Advanced Level)
# ==========================================
print("\n\n" + "="*50)
print("HIGH LEVEL DATA TYPES (Advanced - Specialized)")
print("="*50)

# 1. Complex (complex) - Complex numbers
print("\n1. COMPLEX (complex) - Complex Numbers")
print("-" * 40)
complex_num = 3 + 4j
pure_imaginary = 5j
complex_calc = (2 + 3j) * (1 - 2j)
print(f"Complex number: {complex_num}, type: {type(complex_num)}")
print(f"Pure imaginary: {pure_imaginary}, type: {type(pure_imaginary)}")
print(f"Complex calculation: {complex_calc}, type: {type(complex_calc)}")

# 2. Range (range) - Immutable sequence of numbers
print("\n2. RANGE (range) - Number Sequences")
print("-" * 40)
numbers_5 = range(5)  # 0 to 4
numbers_1_10 = range(1, 11)  # 1 to 10
even_numbers = range(0, 21, 2)  # 0, 2, 4, ..., 20
print(f"Range(5): {list(numbers_5)}, type: {type(numbers_5)}")
print(f"Range(1,11): {list(numbers_1_10)}, type: {type(numbers_1_10)}")
print(f"Even numbers: {list(even_numbers)}, type: {type(even_numbers)}")

# 3. Frozenset (frozenset) - Immutable set
print("\n3. FROZENSET (frozenset) - Immutable Set")
print("-" * 40)
frozen_set = frozenset([1, 2, 3, 4, 5])
frozen_from_list = frozenset(["a", "b", "c", "a", "b"])  # Duplicates removed
empty_frozen = frozenset()
print(f"Frozen set: {frozen_set}, type: {type(frozen_set)}")
print(f"From list: {frozen_from_list}, type: {type(frozen_from_list)}")
print(f"Empty frozen: {empty_frozen}, type: {type(empty_frozen)}")

# 4. Binary Types
print("\n4. BINARY TYPES")
print("-" * 40)

# Bytes (bytes) - Immutable binary data
byte_data = b"Hello"
byte_numbers = bytes([65, 66, 67])  # ASCII values
print(f"Bytes string: {byte_data}, type: {type(byte_data)}")
print(f"Bytes numbers: {byte_numbers}, type: {type(byte_numbers)}")

# Bytearray (bytearray) - Mutable binary data
byte_array = bytearray(b"Hello")
byte_array[0] = 104  # Change 'H' to 'h'
print(f"Bytearray: {byte_array}, type: {type(byte_array)}")

# Memoryview (memoryview) - Memory view of binary data
memory_view = memoryview(byte_data)
print(f"Memoryview: {memory_view}, type: {type(memory_view)}")

# 5. Advanced Collections (from collections module)
print("\n5. ADVANCED COLLECTIONS (from collections module)")
print("-" * 40)

from collections import deque, Counter, OrderedDict, namedtuple

# Deque (double-ended queue)
dq = deque([1, 2, 3])
dq.append(4)  # Add to right
dq.appendleft(0)  # Add to left
print(f"Deque: {dq}, type: {type(dq)}")

# Counter - Count occurrences
counter = Counter(['a', 'b', 'c', 'a', 'b', 'a'])
word_count = Counter("hello world")
print(f"Counter: {counter}, type: {type(counter)}")
print(f"Word count: {word_count}, type: {type(word_count)}")

# OrderedDict - Dictionary that remembers insertion order
ordered_dict = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(f"OrderedDict: {ordered_dict}, type: {type(ordered_dict)}")

# Namedtuple - Tuple with named fields
Point = namedtuple('Point', ['x', 'y'])
p1 = Point(10, 20)
p2 = Point(x=5, y=15)
print(f"Namedtuple Point: {p1}, type: {type(p1)}")
print(f"Namedtuple with kwargs: {p2}, type: {type(p2)}")

print("\n" + "="*50)
print("HIGH LEVEL SUMMARY")
print("="*50)
print("[OK] complex - Complex numbers with real and imaginary parts")
print("[OK] range - Efficient sequences for loops")
print("[OK] frozenset - Immutable sets (can't be modified)")
print("[OK] bytes/bytearray/memoryview - Binary data handling")
print("[OK] deque - Double-ended queues")
print("[OK] Counter - Count occurrences of elements")
print("[OK] OrderedDict - Dictionaries with guaranteed order")
print("[OK] namedtuple - Tuples with named fields")
print("\nThese are specialized types for specific use cases!")

# ==========================================
# TYPE CONVERSION & UTILITIES
# ==========================================
print("\n\n" + "="*50)
print("TYPE CONVERSION & UTILITIES")
print("="*50)

print("\n=== Type Conversion Examples ===")
# Basic conversions
int_to_float = float(42)
float_to_int = int(3.14)
num_to_str = str(123)
str_to_int = int("456")
list_to_tuple = tuple([1, 2, 3])
tuple_to_list = list((4, 5, 6))
list_to_set = set([1, 2, 2, 3, 3, 3])

print(f"int to float: {42} -> {int_to_float} ({type(int_to_float)})")
print(f"float to int: {3.14} -> {float_to_int} ({type(float_to_int)})")
print(f"num to str: {123} -> {num_to_str} ({type(num_to_str)})")
print(f"str to int: {'456'} -> {str_to_int} ({type(str_to_int)})")
print(f"list to tuple: {[1, 2, 3]} -> {list_to_tuple} ({type(list_to_tuple)})")
print(f"tuple to list: {(4, 5, 6)} -> {tuple_to_list} ({type(tuple_to_list)})")
print(f"list to set: {[1, 2, 2, 3, 3, 3]} -> {list_to_set} ({type(list_to_set)})")

print("\n=== Type Checking ===")
data = [1, 2, 3]
print(f"isinstance({data}, list): {isinstance(data, list)}")
print(f"type({data}) == list: {type(data) == list}")

print("\n=== Mutable vs Immutable ===")
print("Mutable types can be changed after creation:")
mutable_list = [1, 2, 3]
print(f"Original: {mutable_list}")
mutable_list.append(4)
print(f"Modified: {mutable_list}")

print("\nImmutable types cannot be changed after creation:")
immutable_tuple = (1, 2, 3)
print(f"Original: {immutable_tuple}")
# immutable_tuple[0] = 0  # This would cause an error!

# ==========================================
# FINAL SUMMARY
# ==========================================
print("\n\n" + "="*60)
print("COMPLETE PYTHON DATA TYPES SUMMARY")
print("="*60)

print("\n[BEGINNER] LOW LEVEL (Beginner - Learn First):")
print("  • int, float, str, bool, NoneType")

print("\n[INTERMEDIATE] MEDIUM LEVEL (Intermediate - Build Understanding):")
print("  • list, tuple, dict, set")

print("\n[ADVANCED] HIGH LEVEL (Advanced - Specialized Use Cases):")
print("  • complex, range, frozenset")
print("  • bytes, bytearray, memoryview")
print("  • deque, Counter, OrderedDict, namedtuple")

print("\n[KEY] KEY CONCEPTS:")
print("  • Mutable vs Immutable")
print("  • Ordered vs Unordered")
print("  • Type conversion")
print("  • Memory efficiency")

print("\n[TIP] TIP: Start with low level, master medium level, then explore high level as needed!")
print("="*60)
# ==========================================
# PRACTICE EXERCISES - Test Your Knowledge!
# ==========================================
print("\n\n" + "="*60)
print("PRACTICE EXERCISES - Test Your Knowledge!")
print("="*60)

print("\n EXERCISE 1: Data Type Identification")
print("-" * 40)
# What data types are these values?
test_values = [
    42,
    3.14,
    "Hello World",
    True,
    [1, 2, 3],
    (4, 5, 6),
    {"name": "Alice", "age": 25},
    {7, 8, 9},
    None,
    2 + 3j
]

for i, value in enumerate(test_values, 1):
    print(f"{i}. {value!r} -> {type(value).__name__}")

print("\n EXERCISE 2: Type Conversion Practice")
print("-" * 40)
original_values = [3.14, "123", [1, 2, 3], (4, 5, 6)]
target_types = ["int", "int", "tuple", "list"]

for i, (value, target) in enumerate(zip(original_values, target_types), 1):
    if target == "int":
        if isinstance(value, float):
            converted = int(value)
        elif isinstance(value, str):
            converted = int(value)
    elif target == "tuple":
        converted = tuple(value)
    elif target == "list":
        converted = list(value)

    print(f"{i}. {value!r} ({type(value).__name__}) -> {converted!r} ({type(converted).__name__})")

print("\n EXERCISE 3: Mutable vs Immutable Demonstration")
print("-" * 40)

# Mutable example
print("Mutable (list):")
mutable_list = [1, 2, 3]
print(f"Original: {mutable_list}")
mutable_list.append(4)
mutable_list[0] = 99
print(f"Modified: {mutable_list}")

# Immutable example
print("\nImmutable (tuple):")
immutable_tuple = (1, 2, 3)
print(f"Original: {immutable_tuple}")
# immutable_tuple[0] = 99  # This would cause an error!
# immutable_tuple.append(4)  # This would cause an error!
print("Cannot modify immutable objects directly!")

print("\n EXERCISE 4: Collections Operations")
print("-" * 40)

# List operations
fruits = ["apple", "banana", "cherry"]
print(f"Original list: {fruits}")
fruits.append("orange")
fruits.insert(1, "grape")
print(f"After adding: {fruits}")

# Dictionary operations
student = {"name": "Alice", "grade": "A"}
print(f"\nOriginal dict: {student}")
student["age"] = 20
student["grade"] = "A+"
print(f"After updating: {student}")

# Set operations
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(f"\nSet1: {set1}, Set2: {set2}")
print(f"Union: {set1 | set2}")
print(f"Intersection: {set1 & set2}")
print(f"Difference: {set1 - set2}")

print("\n EXERCISE 5: Advanced Types Usage")
print("-" * 40)

# Range for loops
print("Range usage:")
for i in range(1, 6):
    print(f"Number: {i}", end=" ")
print()

# Counter example
from collections import Counter
text = "hello world hello python"
word_counts = Counter(text.split())
print(f"\nWord counts: {word_counts}")

# Namedtuple example
from collections import namedtuple
Person = namedtuple('Person', ['name', 'age', 'city'])
person1 = Person("Bob", 30, "New York")
print(f"\nNamedtuple: {person1}")
print(f"Access by name: {person1.name}, {person1.age} years old from {person1.city}")

print("\n" + "="*60)
print("CONGRATULATIONS! You've completed the Python Data Types Tutorial!")
print("="*60)
print("Key takeaways:")
print("• Python has many built-in data types for different purposes")
print("• Choose the right data type for your specific use case")
print("• Understand mutability: lists/dicts/sets can change, tuples/strings/frozensets cannot")
print("• Type conversion helps move between different data types")
print("• Collections module provides advanced data structures")
print("\nReady for the next topic? Let's explore operators, conditionals, or loops!")
print("="*60)

# Interactive section (uncomment to use)
"""
print("\n🔍 INTERACTIVE QUIZ - Uncomment this section to test yourself!")

# Quiz questions
questions = [
    "What data type is 42?",
    "What data type is 3.14?",
    "What data type is 'Hello'?",
    "What data type is True?",
    "What data type is [1, 2, 3]?",
    "What data type is (1, 2, 3)?",
    "What data type is {'key': 'value'}?",
    "What data type is {1, 2, 3}?",
    "What data type is None?",
    "What data type is 2+3j?"
]

answers = ["int", "float", "str", "bool", "list", "tuple", "dict", "set", "NoneType", "complex"]

for i, (q, a) in enumerate(zip(questions, answers), 1):
    user_answer = input(f"{i}. {q} ").strip().lower()
    if user_answer == a.lower():
        print("Correct!")
    else:
        print(f" Wrong! The correct answer is: {a}")
    print()
"""