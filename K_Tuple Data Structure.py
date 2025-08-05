### ✅ 1. **Tuple Creation (Different Ways with Different Data Types)**
# With parentheses
t1 = (1, 2, 3)
# Without parentheses (comma is key)
t2 = 1, 2.5, "Hello"
# Single element tuple
t3 = (10,)  # comma is mandatory
print(t1, t2, t3)


### ✅ 2. **Indexing Tuple**
t = ('a', 'b', 'c', 'd')
print(t[0])  # Output: 'a'
print(t[-1]) # Output: 'd'


### ✅ 3. **Indexing in Nested Tuple**
t = (1, (2, 3), (4, (5, 6)))
print(t[1][1])    # Output: 3
print(t[2][1][0]) # Output: 5


### ✅ 4. **Slicing (All Ways)**
t = (0, 1, 2, 3, 4, 5)
print(t[1:4])   # (1, 2, 3)
print(t[:3])    # (0, 1, 2)
print(t[3:])    # (3, 4, 5)
print(t[:-1])   # (0, 1, 2, 3, 4)
print(t[::-1])  # (5, 4, 3, 2, 1, 0)


### ✅ 5. **Changing a Tuple (Why Not Possible)**
t = (1, 2, 3)
# t[0] = 10  # ❌ Error: 'tuple' object does not support item assignment


### ✅ 6. **Changing an Element in Tuple if It's Mutable**
t = ([1, 2], 3)
t[0][0] = 99  # ✅ Allowed because list is mutable
print(t)      # ([99, 2], 3)


### ✅ 7. **Concatenate Tuples**
t1 = (1, 2)
t2 = (3, 4)
t3 = t1 + t2
print(t3)  # (1, 2, 3, 4)


### ✅ 8. **Repeating the Elements of a Tuple**
t = (1, 2)
print(t * 3)  # (1, 2, 1, 2, 1, 2)


### ✅ 9. **Tuple Deletion**
t = (1, 2, 3)
del t
# print(t)  # ❌ NameError: t is not defined


### ✅ 10. **Tuple `count()` Function**
t = (1, 2, 2, 3, 2)
print(t.count(2))  # 3


### ✅ 11. **`index()` Function**
t = (10, 20, 30, 20)
print(t.index(20))  # 1 (first occurrence)


### ✅ 12. **Tuple Membership**
t = ('a', 'b', 'c')
print('b' in t)     # True
print('z' not in t) # True


### ✅ 13. **`len()` Function**
t = (10, 20, 30)
print(len(t))  # 3


### ✅ 14. **`sorted()` Function**
t = (3, 1, 2)
print(sorted(t))    # [1, 2, 3] (returns a list)


### ✅ 15. **`max()`, `min()`, `sum()` Functions**
t = (4, 7, 1)
print(max(t))  # 7
print(min(t))  # 1
print(sum(t))  # 12
