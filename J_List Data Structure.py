## ✅ 1. List Creation (Different Ways)
# Using square brackets
a = [1, 2, 3]

# Using list() constructor
b = list((4, 5, 6))  # Note: input must be iterable

# Using list comprehension
c = [i for i in range(3)]

# Creating empty list
d = []
e = list()

# From string
f = list("hello")  # ['h', 'e', 'l', 'l', 'o']


## ✅ 2. Length of List
# len() returns number of elements in the list
print(len(a))  # 3


## ✅ 3. Append (Only one way)
# append() adds a single element to the end
a.append(4)


## ✅ 4. Insert (Only one standard way)
# insert(index, element) inserts element at specified position
a.insert(1, 100)


## ✅ 5. Remove Elements from List
### a. remove()
# remove(value) removes first occurrence of the value
a.remove(100)

### b. pop()
# pop() removes and returns last element or element at index
last = a.pop()
second = a.pop(1)

### c. del
# del deletes element at index or entire list
del a[0]     # Removes element at index 0
del a[:]     # Clears list
del a        # Deletes entire list


## ✅ 6. Extend List
### a. Using extend()
# extend() adds all items from another iterable to list
a = [1, 2]
a.extend([3, 4])

### b. Using + operator
# + operator concatenates two lists and returns a new one
a = [1, 2]
b = a + [3, 4]

### c. Using += operator
# += extends the list in-place
a += [5, 6]


## ✅ 7. Membership Check – in and not in
# 'in' checks if element exists in list
print(2 in a)       # True

# 'not in' checks if element does not exist
print(10 not in a)  # True


## ✅ 8. Sorting
### a. Using sorted() (returns new list)
# sorted() returns a sorted list without modifying original
nums = [3, 1, 4, 2]
print(sorted(nums))         # [1, 2, 3, 4]
print(sorted(nums, reverse=True))  # [4, 3, 2, 1]

### b. Using sort() (in-place)
# sort() sorts the list in-place
nums.sort()
nums.sort(reverse=True)  # Descending

### c. Sorting custom keys
# Sorting by custom key
words = ["banana", "apple", "cherry"]
words.sort(key=len)  # Sort by length


## ✅ 9. Reverse
### a. reverse() method
# reverse() reverses list in-place
a = [1, 2, 3]
a.reverse()

### b. Using slicing
# [::-1] returns reversed copy
b = a[::-1]

### c. Using reversed() function
# reversed() returns an iterator
print(list(reversed(a)))


## ✅ 10. Sorting with Different Types (will cause error)
# Cannot sort list with mixed types (e.g., int + str)
# mixed = [1, "two", 3]
# sorted(mixed)  # Raises TypeError


## ✅ 11. List with Multiple References
# Modifying one reference affects all pointing to same list
a = [1, 2, 3]
b = a
a.append(4)
print(b)  # [1, 2, 3, 4]


## ✅ 12. String to List using split()
### a. Default split by whitespace
# split() with no args splits by whitespace
text = "hello world python"
words = text.split()

### b. Split by delimiter

# split(',') splits by comma
csv = "apple,banana,cherry"
fruits = csv.split(',')


## ✅ 13. Indexing
# Accessing elements using index
a = ['x', 'y', 'z']
print(a[0])    # 'x'
print(a[-1])   # 'z'


## ✅ 14. Slicing
# [start:stop:step]
print(a[0:2])   # ['x', 'y']
print(a[:])     # full list copy
print(a[::-1])  # reversed


## ✅ 15. Counting Elements
# count() returns number of times element appears
nums = [1, 2, 2, 3, 2]
print(nums.count(2))  # 3


## ✅ 16. Looping Over Lists
### a. Simple loop
for item in nums:
    print(item)

### b. With index using range()
for i in range(len(nums)):
    print(i, nums[i])

### c. Using enumerate()
for i, val in enumerate(nums):
    print(f"Index: {i}, Value: {val}")


## ✅ 17. List Without Comprehension
# Traditional loop-based list building
squares = []
for i in range(5):
    squares.append(i * i)


## ✅ 18. List With Comprehension
# List comprehension to create list concisely
squares = [i * i for i in range(5)]


## ✅ 19. Nested List Comprehension – Matrix
### a. Create Matrix (3x3)
# Creating a 3x3 matrix
matrix = [[i + j*3 for i in range(1, 4)] for j in range(3)]
print(matrix)  # [[1,2,3],[4,5,6],[7,8,9]]

### b. Transpose Matrix
# Transposing a matrix using nested list comprehension
transpose = [[row[i] for row in matrix] for i in range(3)]
print(transpose)  # [[1,4,7],[2,5,8],[3,6,9]]
