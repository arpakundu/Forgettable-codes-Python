### 1. abs(x)
#*Returns the absolute value of a number.*

print(abs(-5))  # Output: 5


### 2. all(iterable)
#*Returns True if all elements in the iterable are true.*

print(all([True, 1, 3]))  # Output: True


### 3. dir(object)
#*Returns a list of valid attributes and methods of the object.*

print(dir(str))  # Output: list of string methods


### 4. divmod(a, b)
#*Returns a tuple (quotient, remainder).*

print(divmod(10, 3))  # Output: (3, 1)


### 5. enumerate(iterable)
#*Adds a counter to an iterable.*

for i, val in enumerate(['a', 'b']):
    print(i, val)  # Output: 0 a \n 1 b


### 6. filter(function, iterable)
#*Filters elements where the function returns True.*

print(list(filter(lambda x: x > 0, [-2, 3, 0, 5])))  # Output: [3, 5]


### 7. isinstance(obj, type)
#*Checks if an object is an instance of a specified type.*

print(isinstance(5, int))  # Output: True


### 8. map(function, iterable)
#*Applies a function to each item in the iterable.*

print(list(map(str.upper, ['a', 'b'])))  # Output: ['A', 'B']


### 9. reduce(function, iterable)
#*Applies a rolling computation to sequential pairs.*

from functools import reduce
print(reduce(lambda x, y: x + y, [1, 2, 3]))  # Output: 6
