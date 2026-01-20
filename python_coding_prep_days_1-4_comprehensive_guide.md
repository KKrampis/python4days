# Comprehensive Python Programming Guide: Days 1-4
## *A Deep Dive into Higher-Level Python Concepts for Coding Interviews*

---

This guide presents Python fundamentals not just as syntax, but as abstract concepts and patterns essential for problem-solving in technical interviews.

# Comprehensive Python Programming Guide: Days 1-4 Coding Test Preparation

*An in-depth, abstract exploration of Python fundamentals for coding interviews*

---

## Table of Contents

1. [Day 1 Morning: Lists and Tuples - Deep Dive](#day1-morning)
2. [Day 1 Afternoon: Dictionaries and Sets](#day1-afternoon)
3. [Day 2 Morning: String Manipulation](#day2-morning)
4. [Day 2 Afternoon: Algorithm Complexity](#day2-afternoon)
5. [Day 3 Morning: Functions and Higher-Order Programming](#day3-morning)
6. [Day 3 Afternoon: Recursion and Backtracking](#day3-afternoon)
7. [Day 4 Morning: Object-Oriented Programming](#day4-morning)
8. [Day 4 Afternoon: Problem-Solving Patterns](#day4-afternoon)

---

<a name="day1-morning"></a>
# DAY 1 MORNING: Lists and Tuples - Deep Dive

## The Philosophy of Lists

Lists are Python's fundamental mutable sequence type. Understanding lists requires grasping:
- **Dynamic Arrays**: Lists are implemented as resizable arrays
- **Reference Semantics**: Variables hold references, not values
- **Amortized Complexity**: Appending is O(1) amortized, not always O(1)

```python
# Lists are reference types - understanding aliasing
original = [1, 2, 3]
reference = original
reference.append(4)
print(original)  # [1, 2, 3, 4] - both modified!

# Creating true copies
shallow_copy = original.copy()  # or original[:]
import copy
deep_copy = copy.deepcopy(original)  # for nested structures
```

### Performance Characteristics

Understanding what happens "under the hood":

```python
"""
Operation          Time Complexity    Why?
---------          ---------------    ----
list.append(x)     O(1) amortized    Exponential over-allocation
list.insert(0, x)  O(n)              Shifts all elements right
list.pop()         O(1)              Remove from end
list.pop(0)        O(n)              Shifts all elements left
x in list          O(n)              Linear search
list[i]            O(1)              Direct index access
list[i:j]          O(k)              k = j - i (slice size)
list.sort()        O(n log n)        Timsort algorithm
```

### List Comprehensions - Functional Thinking

List comprehensions represent the functional programming paradigm of map-filter-reduce:

```python
# The anatomy of a list comprehension
# [expression for item in iterable if condition]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Map: transform each element
squares = [x**2 for x in numbers]

# Filter: select elements matching condition
evens = [x for x in numbers if x % 2 == 0]

# Map + Filter combined
even_squares = [x**2 for x in numbers if x % 2 == 0]

# Nested comprehensions - matrix operations
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [item for row in matrix for item in row]
# Result: [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Transpose matrix
transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
# Result: [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
```

### Advanced Slicing Patterns

```python
arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Basic slicing [start:stop:step]
arr[2:7]      # [2, 3, 4, 5, 6]
arr[::2]      # [0, 2, 4, 6, 8] - every 2nd element
arr[::-1]     # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0] - reverse

# Negative indices
arr[-3:]      # [7, 8, 9] - last 3 elements
arr[:-3]      # [0, 1, 2, 3, 4, 5, 6] - all but last 3

# Slice assignment - powerful mutation
arr[2:5] = [99, 99, 99]  # Replace elements
arr[2:5] = []            # Delete elements
arr[2:2] = [99]          # Insert element

# Step slicing for patterns
arr[::3]      # Every 3rd element
arr[1::2]     # Odd-indexed elements
arr[2:8:2]    # Elements at indices 2, 4, 6
```

### The Two-Pointer Technique

A fundamental algorithm pattern using list indices:

```python
def two_sum_sorted(numbers, target):
    """
    Find indices of two numbers that sum to target in sorted array.
    
    Concept: Use sorted property to eliminate search space.
    One pointer starts at beginning, one at end.
    Time: O(n), Space: O(1)
    """
    left, right = 0, len(numbers) - 1
    
    while left < right:
        current_sum = numbers[left] + numbers[right]
        
        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1  # Need larger sum
        else:
            right -= 1  # Need smaller sum
    
    return None

def remove_duplicates_sorted(nums):
    """
    Remove duplicates from sorted array in-place.
    
    Concept: Slow pointer marks unique position,
    fast pointer scans for different elements.
    """
    if not nums:
        return 0
    
    slow = 0  # Last unique element position
    
    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]
    
    return slow + 1  # Length of unique portion
```

## Understanding Tuples

Tuples are immutable sequences - a design choice with important implications.

### Immutability as a Feature

```python
# Tuples cannot be modified
point = (10, 20)
# point[0] = 15  # TypeError!

# But objects within tuples can change if mutable
nested = ([1, 2], [3, 4])
nested[0].append(3)  # This works! [1, 2, 3]
# The tuple still references the same list objects

# Tuples as dictionary keys (lists cannot be)
coordinates = {
    (0, 0): "origin",
    (1, 0): "right",
    (0, 1): "up"
}

# Tuples for multiple return values
def get_stats(numbers):
    return min(numbers), max(numbers), sum(numbers)/len(numbers)

minimum, maximum, average = get_stats([1, 2, 3, 4, 5])
```

### Named Tuples - Lightweight Data Classes

```python
from collections import namedtuple

# Define a record type
Point = namedtuple('Point', ['x', 'y'])
Person = namedtuple('Person', 'name age occupation')

# Create instances
p1 = Point(10, 20)
p2 = Point(x=15, y=25)

person = Person("Alice", 30, "Engineer")

# Access by name or position
print(p1.x, p1.y)    # 10 20
print(p1[0], p1[1])  # 10 20

# Immutability preserved
# person.age = 31  # AttributeError

# Useful for CSV/database rows
Employee = namedtuple('Employee', 'id name department salary')
employees = [
    Employee(1, "Alice", "Engineering", 100000),
    Employee(2, "Bob", "Sales", 80000)
]

# Sort by field
by_salary = sorted(employees, key=lambda e: e.salary, reverse=True)
```

### Tuple Packing and Unpacking

```python
# Packing - creating tuples implicitly
coordinates = 10, 20, 30  # (10, 20, 30)

# Unpacking - destructuring
x, y, z = coordinates

# Extended unpacking with *
first, *middle, last = [1, 2, 3, 4, 5]
# first=1, middle=[2,3,4], last=5

# Swapping variables elegantly
a, b = 10, 20
a, b = b, a  # Swap using tuple packing/unpacking

# Unpacking in function calls
def func(a, b, c):
    return a + b + c

args = (1, 2, 3)
result = func(*args)  # Unpacks tuple as arguments

# Ignoring values with _
x, _, z = (1, 2, 3)  # Ignore middle value

# Nested unpacking
data = [('Alice', 30), ('Bob', 25)]
for name, age in data:
    print(f"{name} is {age}")
```



<a name="day1-afternoon"></a>
# DAY 1 AFTERNOON: Dictionaries and Sets

## The Hash Table Abstraction

Dictionaries implement the hash table data structure - mapping keys to values with O(1) average-case lookup.

### Understanding Hashing

```python
# Hash functions map objects to integers
print(hash("hello"))  # Some integer (consistent per session)
print(hash(42))       # 42 (integers hash to themselves for small values)
print(hash((1, 2)))   # Tuples are hashable if contents are

# Only immutable objects can be hashed
try:
    hash([1, 2, 3])  # TypeError: unhashable type: 'list'
except TypeError:
    print("Lists cannot be dictionary keys!")

# Why? If a key's hash changes, the dictionary breaks
```

### Dictionary Operations and Patterns

```python
# Creating dictionaries
empty = {}
empty = dict()

# From key-value pairs
pairs = dict([('a', 1), ('b', 2), ('c', 3)])

# From keyword arguments
person = dict(name="Alice", age=30, city="NYC")

# Dictionary comprehension
squares = {x: x**2 for x in range(10)}
inverted = {v: k for k, v in pairs.items()}  # Swap keys and values

# Safe key access
value = my_dict.get('key', default_value)  # Returns default if key missing
value = my_dict.setdefault('key', default)  # Sets and returns default if missing

# Update with another dictionary
dict1.update(dict2)  # Merge dict2 into dict1
merged = {**dict1, **dict2}  # Python 3.5+
merged = dict1 | dict2  # Python 3.9+
```

### Default Dictionary Pattern

```python
from collections import defaultdict

# Group items by property
def group_by_length(words):
    groups = defaultdict(list)
    for word in words:
        groups[len(word)].append(word)
    return dict(groups)

words = ["a", "bb", "ccc", "dd", "e", "fff", "gg"]
grouped = group_by_length(words)
# {1: ['a', 'e'], 2: ['bb', 'dd', 'gg'], 3: ['ccc', 'fff']}

# Count occurrences (better: use Counter)
def count_chars(text):
    counts = defaultdict(int)
    for char in text:
        counts[char] += 1
    return dict(counts)

# Build graph adjacency list
def build_graph(edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
    return dict(graph)
```

### Counter - Frequency Counting

```python
from collections import Counter

# Count element frequencies
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
counts = Counter(words)
# Counter({'apple': 3, 'banana': 2, 'cherry': 1})

# Most common elements
top_2 = counts.most_common(2)
# [('apple', 3), ('banana', 2)]

# Counter arithmetic
c1 = Counter(a=3, b=1, c=1)
c2 = Counter(a=1, b=2, d=1)

c1 + c2  # Counter({'a': 4, 'b': 3, 'c': 1, 'd': 1})
c1 - c2  # Counter({'a': 2}) - only positive counts
c1 & c2  # Intersection: Counter({'a': 1, 'b': 1})
c1 | c2  # Union: Counter({'a': 3, 'b': 2, 'c': 1, 'd': 1})

# Character frequency in string
text = "hello world"
char_freq = Counter(text)
```

## Sets - The Mathematical Abstraction

Sets provide the mathematical set operations with O(1) membership testing.

### Set Operations

```python
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# Union - elements in either set
union = A | B              # {1, 2, 3, 4, 5, 6, 7, 8}
union = A.union(B)

# Intersection - elements in both
intersection = A & B       # {4, 5}
intersection = A.intersection(B)

# Difference - in A but not B
difference = A - B         # {1, 2, 3}
difference = A.difference(B)

# Symmetric difference - in either but not both
sym_diff = A ^ B           # {1, 2, 3, 6, 7, 8}
sym_diff = A.symmetric_difference(B)

# Subset/superset
{1, 2}.issubset(A)         # True
A.issuperset({1, 2})       # True
A.isdisjoint(B)            # False (they share elements)
```

### Common Set Patterns

```python
# Remove duplicates
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
unique = list(set(numbers))

# Fast membership testing
# Anti-pattern: O(n) list search
if target in large_list:  # Slow!
    pass

# Optimal: O(1) set lookup
large_set = set(large_list)
if target in large_set:   # Fast!
    pass

# Find missing number
def find_missing(nums):
    n = len(nums)
    expected = set(range(n + 1))
    actual = set(nums)
    return (expected - actual).pop()

# Find duplicates
def find_duplicates(nums):
    seen = set()
    dupes = set()
    for num in nums:
        if num in seen:
            dupes.add(num)
        seen.add(num)
    return dupes

# Common elements across multiple lists
def common_elements(*lists):
    if not lists:
        return set()
    result = set(lists[0])
    for lst in lists[1:]:
        result &= set(lst)
    return result
```

---

<a name="day2-morning"></a>
# DAY 2 MORNING: String Manipulation and Patterns

## The Immutability of Strings

Strings in Python are immutable - every "modification" creates a new string.

### Performance Implications

```python
# Anti-pattern: O(n²) due to repeated string creation
result = ""
for i in range(1000):
    result += str(i)  # Creates 1000 intermediate strings!

# Optimal: O(n) using join
result = "".join(str(i) for i in range(1000))

# Why? Each += creates a new string and copies all previous characters
# join() calculates total size and allocates once
```

### String Methods - Transformation Toolkit

```python
text = "  Hello, World!  "

# Case transformations
text.upper()      # '  HELLO, WORLD!  '
text.lower()      # '  hello, world!  '
text.title()      # '  Hello, World!  '
text.capitalize() # '  hello, world!  '
text.swapcase()   # '  hELLO, wORLD!  '

# Whitespace handling
text.strip()      # 'Hello, World!'
text.lstrip()     # 'Hello, World!  '
text.rstrip()     # '  Hello, World!'
text.strip('! ')  # 'Hello, World' - strip specific chars

# Searching
'World' in text           # True
text.startswith('  Hello') # True
text.endswith('!  ')      # True
text.find('World')        # 9 (-1 if not found)
text.index('World')       # 9 (raises ValueError if not found)
text.count('l')           # 3

# Replacing
text.replace('World', 'Python')
text.replace('l', 'L', 2)  # Replace first 2 occurrences
```

### Splitting and Joining

```python
# Split operations
sentence = "The quick brown fox"
words = sentence.split()  # Split on whitespace
# ['The', 'quick', 'brown', 'fox']

csv_line = "apple,banana,cherry"
fruits = csv_line.split(',')
# ['apple', 'banana', 'cherry']

# Limit splits
"a:b:c:d".split(':', 2)  # ['a', 'b', 'c:d']

# splitlines - handle different line endings
multiline = "line1\nline2\r\nline3"
lines = multiline.splitlines()

# Join - inverse of split
" ".join(words)      # "The quick brown fox"
", ".join(fruits)    # "apple, banana, cherry"

# Efficient path building
import os
path = os.path.join('folder', 'subfolder', 'file.txt')
```

### String Formatting Evolution

```python
name = "Alice"
age = 30
pi = 3.14159265359

# Old-style % formatting
"Name: %s, Age: %d" % (name, age)

# str.format()
"Name: {}, Age: {}".format(name, age)
"Name: {n}, Age: {a}".format(n=name, a=age)
"Pi: {:.2f}".format(pi)  # '3.14'

# f-strings (Python 3.6+) - PREFERRED
f"Name: {name}, Age: {age}"
f"Pi: {pi:.2f}"
f"Calculation: {2 + 2 = }"  # Python 3.8+: 'Calculation: 2 + 2 = 4'

# Advanced formatting
value = 1234567.89
f"{value:,.2f}"        # '1,234,567.89' - thousands separator
f"{value:>15.2f}"      # '     1234567.89' - right-align in width 15
f"{age:05d}"           # '00030' - zero-pad to 5 digits
f"{name:^20}"          # '       Alice        ' - center in width 20
```

### Regular Expressions - Pattern Matching

```python
import re

# Basic patterns
text = "The price is $19.99 and $29.99"

# Search - find first match
match = re.search(r'\$(\d+\.\d+)', text)
if match:
    price = match.group(1)  # '19.99'

# findall - find all matches
prices = re.findall(r'\$(\d+\.\d+)', text)
# ['19.99', '29.99']

# Match groups
pattern = r'(\d{3})-(\d{4})'
match = re.search(pattern, "Call 555-1234")
area_code, number = match.groups()  # ('555', '1234')

# Replace with pattern
cleaned = re.sub(r'\s+', ' ', "too    many     spaces")
# 'too many spaces'

# Split on pattern
parts = re.split(r'[,;]\s*', "apple, banana; cherry")
# ['apple', 'banana', 'cherry']

# Compiled patterns for efficiency
email_regex = re.compile(r'^[\w.-]+@[\w.-]+\.\w+$')
is_valid = email_regex.match("user@example.com")

# Common patterns
patterns = {
    'email': r'^[\w.-]+@[\w.-]+\.\w+$',
    'phone': r'^\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}$',
    'url': r'https?://[^\s]+',
    'date': r'\d{4}-\d{2}-\d{2}',
    'hashtag': r'#\w+',
    'mention': r'@\w+'
}
```

### String Algorithm Patterns

```python
# Palindrome checking
def is_palindrome(s):
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]

# Anagram detection
def are_anagrams(s1, s2):
    return sorted(s1.lower()) == sorted(s2.lower())

# Alternative with Counter
from collections import Counter
def are_anagrams_counter(s1, s2):
    return Counter(s1.lower()) == Counter(s2.lower())

# Longest substring without repeating characters
def longest_unique_substring(s):
    char_index = {}
    max_length = 0
    start = 0
    
    for end, char in enumerate(s):
        if char in char_index and char_index[char] >= start:
            start = char_index[char] + 1
        
        char_index[char] = end
        max_length = max(max_length, end - start + 1)
    
    return max_length

# Sliding window for substring patterns
def find_all_substrings(s, length):
    return [s[i:i+length] for i in range(len(s) - length + 1)]
```

---

<a name="day2-afternoon"></a>
# DAY 2 AFTERNOON: Algorithm Complexity and Sorting

## Big O Notation - Growth Rate Analysis

Big O describes the upper bound of algorithm complexity as input size approaches infinity.

### Common Complexity Classes

```python
# O(1) - Constant time
def get_first(arr):
    return arr[0] if arr else None

# O(log n) - Logarithmic
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# O(n) - Linear
def find_max(arr):
    return max(arr) if arr else None

# O(n log n) - Linearithmic
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

# O(n²) - Quadratic
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# O(2ⁿ) - Exponential
def fibonacci_naive(n):
    if n <= 1:
        return n
    return fibonacci_naive(n - 1) + fibonacci_naive(n - 2)
```

### Complexity Analysis Principles

```python
# Rule 1: Drop constants
# O(2n) = O(n), O(n/2) = O(n)

# Rule 2: Drop lower-order terms
# O(n² + n) = O(n²), O(n log n + n) = O(n log n)

# Rule 3: Different inputs = different variables
def process_two_arrays(arr1, arr2):
    # O(n + m), NOT O(n)
    for x in arr1:  # O(n)
        print(x)
    for y in arr2:  # O(m)
        print(y)

# Rule 4: Nested loops multiply
def find_pairs(arr1, arr2):
    # O(n * m)
    for x in arr1:
        for y in arr2:
            print(x, y)
```

## Sorting Algorithms - Deep Understanding

### Comparison-Based Sorts

```python
# Insertion Sort - O(n²), but O(n) when nearly sorted
def insertion_sort(arr):
    """
    Build sorted array one element at a time.
    Like sorting playing cards in your hand.
    
    Best: O(n) when already sorted
    Worst: O(n²) when reverse sorted
    Space: O(1) in-place
    Stable: Yes
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Merge Sort - O(n log n) always
def merge_sort(arr):
    """
    Divide and conquer with merging.
    
    Time: O(n log n) - always
    Space: O(n) for temporary arrays
    Stable: Yes
    
    Reliable performance for large datasets.
    """
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    # Merge sorted halves
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Quick Sort - O(n log n) average, O(n²) worst
def quick_sort(arr):
    """
    Partition around pivot, recursively sort.
    
    Time: O(n log n) average, O(n²) worst
    Space: O(log n) recursion stack
    Stable: No
    
    Often fastest in practice due to cache locality.
    """
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)

# Heap Sort - O(n log n) always, O(1) space
def heap_sort(arr):
    """
    Use heap data structure for sorting.
    
    Time: O(n log n) - always
    Space: O(1) in-place
    Stable: No
    
    Guaranteed performance with minimal space.
    """
    def heapify(arr, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        
        if left < n and arr[left] > arr[largest]:
            largest = left
        if right < n and arr[right] > arr[largest]:
            largest = right
        
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)
    
    n = len(arr)
    
    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    
    # Extract elements
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)
    
    return arr
```

### Non-Comparison Sorts

```python
# Counting Sort - O(n + k)
def counting_sort(arr, max_val=None):
    """
    Count occurrences and reconstruct.
    
    Time: O(n + k) where k is range
    Space: O(k)
    Stable: Yes (with careful implementation)
    
    Efficient when range is not much larger than n.
    """
    if not arr:
        return arr
    
    if max_val is None:
        max_val = max(arr)
    
    counts = [0] * (max_val + 1)
    
    for num in arr:
        counts[num] += 1
    
    result = []
    for num, count in enumerate(counts):
        result.extend([num] * count)
    
    return result

# Radix Sort - O(d * (n + k))
def radix_sort(arr):
    """
    Sort by individual digits.
    
    Time: O(d * (n + k)) where d is number of digits
    Space: O(n + k)
    Stable: Yes
    
    Efficient for integers with fixed number of digits.
    """
    if not arr:
        return arr
    
    max_num = max(arr)
    exp = 1
    
    while max_num // exp > 0:
        counting_sort_by_digit(arr, exp)
        exp *= 10
    
    return arr

def counting_sort_by_digit(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10
    
    for num in arr:
        digit = (num // exp) % 10
        count[digit] += 1
    
    for i in range(1, 10):
        count[i] += count[i - 1]
    
    for i in range(n - 1, -1, -1):
        digit = (arr[i] // exp) % 10
        output[count[digit] - 1] = arr[i]
        count[digit] -= 1
    
    for i in range(n):
        arr[i] = output[i]
```

---

(Continued in next message due to length...)

<a name="day3-morning"></a>
# DAY 3 MORNING: Functions, Scope, and Higher-Order Programming

## Functions as First-Class Citizens

In Python, functions are objects that can be:
- Assigned to variables
- Passed as arguments
- Returned from functions
- Stored in data structures

```python
# Functions are objects
def square(x):
    return x ** 2

# Assign to variable
my_func = square
print(my_func(5))  # 25

# Store in data structure
operations = {
    'square': square,
    'cube': lambda x: x ** 3,
    'double': lambda x: x * 2
}

result = operations['cube'](4)  # 64

# Pass as argument
def apply_operation(func, value):
    return func(value)

result = apply_operation(square, 10)  # 100
```

### Parameter Passing Mechanisms

```python
# Positional and keyword arguments
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

greet("Alice")                    # "Hello, Alice!"
greet("Bob", "Hi")                # "Hi, Bob!"
greet(greeting="Hey", name="Charlie")  # "Hey, Charlie!"

# *args - variable positional arguments
def sum_all(*numbers):
    return sum(numbers)

sum_all(1, 2, 3, 4, 5)  # 15

# **kwargs - variable keyword arguments
def build_profile(**info):
    return info

profile = build_profile(name="Alice", age=30, city="NYC")

# Combined parameter types (order matters!)
def complex_func(pos1, pos2, *args, kwonly1, kwonly2="default", **kwargs):
    \"""
    Order:
    1. Positional parameters
    2. *args
    3. Keyword-only parameters
    4. **kwargs
    \"""
    pass

# Unpacking in function calls
def func(a, b, c):
    return a + b + c

args = [1, 2, 3]
kwargs = {'a': 1, 'b': 2, 'c': 3}

func(*args)      # Unpack list
func(**kwargs)   # Unpack dictionary
```

### Scope - The LEGB Rule

Python searches for variables in this order: Local, Enclosing, Global, Built-in

```python
x = "global"

def outer():
    x = "enclosing"
    
    def inner():
        x = "local"
        print(x)  # Prints "local"
    
    inner()
    print(x)  # Prints "enclosing"

outer()
print(x)  # Prints "global"

# Modifying outer scopes
counter = 0

def increment():
    global counter  # Modify global variable
    counter += 1

def make_counter():
    count = 0
    
    def increment():
        nonlocal count  # Modify enclosing variable
        count += 1
        return count
    
    return increment
```

### Closures - Capturing Environment

```python
def make_multiplier(factor):
    \"""
    Return function that multiplies by factor.
    The returned function 'closes over' factor.
    \"""
    def multiplier(x):
        return x * factor
    return multiplier

times_2 = make_multiplier(2)
times_10 = make_multiplier(10)

print(times_2(5))   # 10
print(times_10(5))  # 50

# Practical closure: maintaining state
def make_accumulator(initial=0):
    total = initial
    
    def accumulate(value):
        nonlocal total
        total += value
        return total
    
    return accumulate

acc = make_accumulator(100)
print(acc(10))  # 110
print(acc(20))  # 130
print(acc(-30)) # 100
```

### Decorators - Function Wrappers

```python
# Simple decorator
def uppercase_result(func):
    \"""Decorator that uppercases function result.\"""
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper

@uppercase_result
def greet(name):
    return f"hello, {name}"

print(greet("alice"))  # "HELLO, ALICE"

# Decorator with arguments
def repeat(times):
    \"""Decorator that repeats execution.\"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            results = []
            for _ in range(times):
                results.append(func(*args, **kwargs))
            return results
        return wrapper
    return decorator

@repeat(3)
def say_hello():
    return "Hello!"

print(say_hello())  # ['Hello!', 'Hello!', 'Hello!']

# Preserving metadata
from functools import wraps

def my_decorator(func):
    @wraps(func)  # Preserves __name__, __doc__, etc.
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

# Practical decorators
import time

def timer(func):
    \"""Measure execution time.\"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f}s")
        return result
    return wrapper

def memoize(func):
    \"""Cache function results.\"""
    cache = {}
    
    @wraps(func)
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper

@memoize
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# Now O(n) instead of O(2^n)!
```

## Higher-Order Functions

Functions that take functions as arguments or return functions.

```python
# Map - transform each element
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
# [1, 4, 9, 16, 25]

# Filter - keep matching elements
evens = list(filter(lambda x: x % 2 == 0, numbers))
# [2, 4]

# Reduce - combine to single value
from functools import reduce
product = reduce(lambda x, y: x * y, numbers)
# 120

# Function composition
def compose(f, g):
    \"""Return f(g(x)).\"""
    return lambda x: f(g(x))

def double(x):
    return x * 2

def add_ten(x):
    return x + 10

double_then_add = compose(add_ten, double)
print(double_then_add(5))  # (5 * 2) + 10 = 20

# Partial application
from functools import partial

def power(base, exponent):
    return base ** exponent

square = partial(power, exponent=2)
cube = partial(power, exponent=3)

print(square(5))  # 25
print(cube(5))    # 125

# Custom higher-order functions
def apply_twice(func, x):
    return func(func(x))

def add_five(x):
    return x + 5

result = apply_twice(add_five, 0)  # 10

# Pipeline pattern
def pipeline(*functions):
    def apply(x):
        for func in functions:
            x = func(x)
        return x
    return apply

process = pipeline(
    str.strip,
    str.lower,
    lambda s: s.replace(" ", "_")
)

result = process("  Hello World  ")  # "hello_world"
```

---

<a name="day3-afternoon"></a>
# DAY 3 AFTERNOON: Recursion and Backtracking

## Understanding Recursion

Recursion solves problems by breaking them into smaller instances of the same problem.

### The Recursive Mindset

Every recursive solution needs:
1. **Base case(s)** - when to stop
2. **Recursive case(s)** - how to break down the problem
3. **Progress** - each call must move toward base case

```python
# Classic examples
def factorial(n):
    if n == 0:  # Base case
        return 1
    return n * factorial(n - 1)  # Recursive case

def fibonacci(n):
    if n <= 1:  # Base cases
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# Sum of list
def sum_list(numbers):
    if not numbers:  # Base case
        return 0
    return numbers[0] + sum_list(numbers[1:])

# Find maximum
def find_max(arr, n=None):
    if n is None:
        n = len(arr)
    
    if n == 1:  # Base case
        return arr[0]
    
    max_of_rest = find_max(arr, n - 1)
    return max(arr[n - 1], max_of_rest)
```

### Recursion with Memoization

Optimize overlapping subproblems:

```python
def fibonacci_memo(n, memo=None):
    if memo is None:
        memo = {}
    
    if n in memo:
        return memo[n]
    
    if n <= 1:
        return n
    
    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    return memo[n]

# Longest Common Subsequence
def lcs(s1, s2, memo=None):
    if memo is None:
        memo = {}
    
    key = (len(s1), len(s2))
    if key in memo:
        return memo[key]
    
    if not s1 or not s2:
        return 0
    
    if s1[0] == s2[0]:
        result = 1 + lcs(s1[1:], s2[1:], memo)
    else:
        result = max(lcs(s1[1:], s2, memo), lcs(s1, s2[1:], memo))
    
    memo[key] = result
    return result
```

### Tree Recursion

```python
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Tree traversals
def inorder(node):
    \"""Left, Root, Right\"""
    if not node:
        return []
    return inorder(node.left) + [node.val] + inorder(node.right)

def preorder(node):
    \"""Root, Left, Right\"""
    if not node:
        return []
    return [node.val] + preorder(node.left) + preorder(node.right)

def postorder(node):
    \"""Left, Right, Root\"""
    if not node:
        return []
    return postorder(node.left) + postorder(node.right) + [node.val]

# Tree properties
def height(node):
    if not node:
        return 0
    return 1 + max(height(node.left), height(node.right))

def count_nodes(node):
    if not node:
        return 0
    return 1 + count_nodes(node.left) + count_nodes(node.right)

def is_balanced(node):
    def check_height(node):
        if not node:
            return 0
        
        left = check_height(node.left)
        if left == -1:
            return -1
        
        right = check_height(node.right)
        if right == -1:
            return -1
        
        if abs(left - right) > 1:
            return -1
        
        return 1 + max(left, right)
    
    return check_height(node) != -1
```

## Backtracking - Systematic Exploration

Backtracking explores all possibilities by building candidates and abandoning failures.

### The Backtracking Template

```python
def backtrack(candidate):
    if is_solution(candidate):
        process_solution(candidate)
        return
    
    for choice in get_choices(candidate):
        if is_valid(choice):
            make_choice(choice)
            backtrack(candidate)
            unmake_choice(choice)  # Backtrack!
```

### Permutations

```python
def permutations(nums):
    \"""Generate all permutations.\"""
    def backtrack(current, remaining):
        if not remaining:
            result.append(current[:])
            return
        
        for i in range(len(remaining)):
            # Choose
            current.append(remaining[i])
            new_remaining = remaining[:i] + remaining[i+1:]
            
            # Explore
            backtrack(current, new_remaining)
            
            # Unchoose
            current.pop()
    
    result = []
    backtrack([], nums)
    return result

# Alternative with swapping
def permute_swap(nums):
    def backtrack(start):
        if start == len(nums):
            result.append(nums[:])
            return
        
        for i in range(start, len(nums)):
            nums[start], nums[i] = nums[i], nums[start]
            backtrack(start + 1)
            nums[start], nums[i] = nums[i], nums[start]
    
    result = []
    backtrack(0)
    return result
```

### Combinations

```python
def combinations(nums, k):
    \"""Generate all k-element combinations.\"""
    def backtrack(start, current):
        if len(current) == k:
            result.append(current[:])
            return
        
        for i in range(start, len(nums)):
            current.append(nums[i])
            backtrack(i + 1, current)
            current.pop()
    
    result = []
    backtrack(0, [])
    return result

# Subsets (power set)
def subsets(nums):
    def backtrack(start, current):
        result.append(current[:])
        
        for i in range(start, len(nums)):
            current.append(nums[i])
            backtrack(i + 1, current)
            current.pop()
    
    result = []
    backtrack(0, [])
    return result
```

### N-Queens Problem

```python
def solve_n_queens(n):
    \"""Place n queens on n×n board.\"""
    def is_safe(row, col):
        # Check column
        for r in range(row):
            if board[r] == col:
                return False
        
        # Check diagonals
        for r in range(row):
            if abs(board[r] - col) == abs(r - row):
                return False
        
        return True
    
    def backtrack(row):
        if row == n:
            result.append(board[:])
            return
        
        for col in range(n):
            if is_safe(row, col):
                board[row] = col
                backtrack(row + 1)
    
    result = []
    board = [-1] * n
    backtrack(0)
    return result
```

### Sudoku Solver

```python
def solve_sudoku(board):
    \"""Solve 9x9 Sudoku puzzle.\"""
    def is_valid(row, col, num):
        # Check row
        if num in board[row]:
            return False
        
        # Check column
        for r in range(9):
            if board[r][col] == num:
                return False
        
        # Check 3x3 box
        box_row, box_col = 3 * (row // 3), 3 * (col // 3)
        for r in range(box_row, box_row + 3):
            for c in range(box_col, box_col + 3):
                if board[r][c] == num:
                    return False
        
        return True
    
    def backtrack():
        for row in range(9):
            for col in range(9):
                if board[row][col] == 0:
                    for num in range(1, 10):
                        if is_valid(row, col, num):
                            board[row][col] = num
                            
                            if backtrack():
                                return True
                            
                            board[row][col] = 0
                    
                    return False
        return True
    
    backtrack()
    return board
```

---

<a name="day4-morning"></a>
# DAY 4 MORNING: Object-Oriented Programming

## Classes and Objects

OOP organizes code around objects that encapsulate data and behavior.

```python
class Person:
    # Class attribute (shared by all instances)
    species = "Homo sapiens"
    
    def __init__(self, name, age):
        # Instance attributes (unique to each instance)
        self.name = name
        self.age = age
    
    def greet(self):
        \"""Instance method.\"""
        return f"Hello, I'm {self.name}"
    
    @classmethod
    def from_birth_year(cls, name, birth_year):
        \"""Alternative constructor.\"""
        age = 2026 - birth_year
        return cls(name, age)
    
    @staticmethod
    def is_adult(age):
        \"""Utility function in class namespace.\"""
        return age >= 18
    
    def __str__(self):
        return f"Person({self.name}, {self.age})"
    
    def __repr__(self):
        return f"Person('{self.name}', {self.age})"

# Usage
alice = Person("Alice", 30)
bob = Person.from_birth_year("Bob", 1995)
```

### Encapsulation and Properties

```python
class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self._balance = balance  # Protected by convention
        self.__pin = None        # Private (name mangling)
    
    @property
    def balance(self):
        \"""Read-only access to balance.\"""
        return self._balance
    
    @balance.setter
    def balance(self, value):
        if value >= 0:
            self._balance = value
        else:
            raise ValueError("Balance cannot be negative")
    
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            return True
        return False
    
    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            return True
        return False

# Computed properties
class Temperature:
    def __init__(self, celsius=0):
        self._celsius = celsius
    
    @property
    def celsius(self):
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Below absolute zero!")
        self._celsius = value
    
    @property
    def fahrenheit(self):
        return self._celsius * 9/5 + 32
    
    @fahrenheit.setter
    def fahrenheit(self, value):
        self.celsius = (value - 32) * 5/9
    
    @property
    def kelvin(self):
        return self._celsius + 273.15
```

## Inheritance and Polymorphism

```python
class Animal:
    def __init__(self, name):
        self.name = name
    
    def make_sound(self):
        raise NotImplementedError("Subclass must implement")
    
    def eat(self):
        return f"{self.name} is eating"

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
    
    def make_sound(self):
        return "Woof!"
    
    def fetch(self):
        return f"{self.name} is fetching"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

# Polymorphism
animals = [Dog("Rex", "Labrador"), Cat("Whiskers")]
for animal in animals:
    print(f"{animal.name}: {animal.make_sound()}")
```

### Abstract Base Classes

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        import math
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        import math
        return 2 * math.pi * self.radius
```

## Special Methods (Magic Methods)

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return f"Vector({self.x}, {self.y})"
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)
    
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __abs__(self):
        return (self.x**2 + self.y**2) ** 0.5
    
    def __getitem__(self, index):
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        raise IndexError("Vector index out of range")

v1 = Vector(2, 3)
v2 = Vector(4, 1)
v3 = v1 + v2  # Vector(6, 4)
```

---

<a name="day4-afternoon"></a>
# DAY 4 AFTERNOON: Problem-Solving Patterns

## Sliding Window

```python
def max_sum_subarray(arr, k):
    \"""Maximum sum of k consecutive elements.\"""
    window_sum = sum(arr[:k])
    max_sum = window_sum
    
    for i in range(k, len(arr)):
        window_sum = window_sum - arr[i-k] + arr[i]
        max_sum = max(max_sum, window_sum)
    
    return max_sum

def longest_substring_k_distinct(s, k):
    \"""Longest substring with ≤ k distinct characters.\"""
    char_count = {}
    left = 0
    max_length = 0
    
    for right in range(len(s)):
        char_count[s[right]] = char_count.get(s[right], 0) + 1
        
        while len(char_count) > k:
            char_count[s[left]] -= 1
            if char_count[s[left]] == 0:
                del char_count[s[left]]
            left += 1
        
        max_length = max(max_length, right - left + 1)
    
    return max_length
```

## Two Pointers

```python
def is_palindrome(s):
    left, right = 0, len(s) - 1
    
    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        
        if s[left].lower() != s[right].lower():
            return False
        
        left += 1
        right -= 1
    
    return True

def three_sum(nums, target=0):
    \"""Find all triplets that sum to target.\"""
    nums.sort()
    result = []
    
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        
        left, right = i + 1, len(nums) - 1
        
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            
            if total == target:
                result.append([nums[i], nums[left], nums[right]])
                
                while left < right and nums[left] == nums[left+1]:
                    left += 1
                while left < right and nums[right] == nums[right-1]:
                    right -= 1
                
                left += 1
                right -= 1
            elif total < target:
                left += 1
            else:
                right -= 1
    
    return result
```

## Dynamic Programming

```python
def fibonacci_dp(n):
    if n <= 1:
        return n
    
    dp = [0] * (n + 1)
    dp[1] = 1
    
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    
    return dp[n]

def coin_change(coins, amount):
    \"""Minimum coins to make amount.\"""
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    
    for i in range(1, amount + 1):
        for coin in coins:
            if i >= coin:
                dp[i] = min(dp[i], dp[i-coin] + 1)
    
    return dp[amount] if dp[amount] != float('inf') else -1

def longest_increasing_subsequence(nums):
    if not nums:
        return 0
    
    dp = [1] * len(nums)
    
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp)
```

## Binary Search Variations

```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

def find_first(arr, target):
    \"""Find first occurrence.\"""
    left, right = 0, len(arr) - 1
    result = -1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            result = mid
            right = mid - 1  # Continue left
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return result

def search_rotated(arr, target):
    \"""Search in rotated sorted array.\"""
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        
        if arr[left] <= arr[mid]:  # Left half sorted
            if arr[left] <= target < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:  # Right half sorted
            if arr[mid] < target <= arr[right]:
                left = mid + 1
            else:
                right = mid - 1
    
    return -1
```

## Graph Traversal

```python
from collections import deque

def bfs(graph, start):
    \"""Breadth-First Search.\"""
    visited = set([start])
    queue = deque([start])
    
    while queue:
        node = queue.popleft()
        print(node)
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

def dfs_recursive(graph, node, visited=None):
    \"""Depth-First Search (recursive).\"""
    if visited is None:
        visited = set()
    
    visited.add(node)
    print(node)
    
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)

def dfs_iterative(graph, start):
    \"""Depth-First Search (iterative).\"""
    visited = set()
    stack = [start]
    
    while stack:
        node = stack.pop()
        
        if node not in visited:
            visited.add(node)
            print(node)
            
            for neighbor in reversed(graph[node]):
                if neighbor not in visited:
                    stack.append(neighbor)
```

---

## Summary and Practice Strategy

This comprehensive guide has covered:

**Day 1**: Core data structures (lists, tuples, dicts, sets) with deep understanding of performance and abstractions

**Day 2**: String manipulation, regular expressions, algorithm complexity, and sorting algorithms

**Day 3**: Functions as first-class objects, closures, decorators, recursion, and backtracking

**Day 4**: Object-oriented programming and essential problem-solving patterns

### Practice Recommendations:

1. **Implement everything yourself** - Code each pattern multiple times
2. **Solve variations** - Find 3-5 similar problems for each pattern
3. **Analyze complexity** - Always consider time and space trade-offs
4. **Explain your thinking** - Verbalize your approach as if in an interview
5. **Build intuition** - Understand WHY each technique works, not just HOW

Master these fundamentals and you'll have a strong foundation for tackling any coding interview challenge!

