### ✅ 1. **Set Creation (Different Ways with Different Data Types)**
s1 = {1, 2, 3}              # Integers
s2 = {'a', 'b', 'c'}        # Strings
s3 = {1, "hi", 3.5, True}   # Mixed types
print(s1, s2, s3)


### ✅ 2. **Set Creation with `set()`**
s = set([1, 2, 3])
print(s)  # {1, 2, 3}


### ✅ 3. **Making a Set from a List**
lst = [1, 2, 2, 3, 3, 3]
s = set(lst)
print(s)  # {1, 2, 3}


### ✅ 4. **Set Does Not Allow Duplicate Items**
s = {1, 2, 2, 3, 3}
print(s)  # {1, 2, 3}


### ✅ 5. **`add()`, `update()`**
s = {1, 2}
s.add(3)
s.update([4, 5], {6, 7})
print(s)  # {1, 2, 3, 4, 5, 6, 7}


### ✅ 6. **Adding a List or Set (Nested Inside)**
s = {1, 2}
# s.add([3, 4])  # ❌ Error: list is unhashable
s.add((3, 4))     # ✅ Tuples are hashable
print(s)

s2 = {10, 20}
s.update({30, 40})
print(s2)         # {10, 20, 30, 40}


### ✅ 7. **Remove Elements with `discard()`**
s = {1, 2, 3}
s.discard(2)
s.discard(5)  # No error if not present
print(s)      # {1, 3}


### ✅ 8. **`remove()`, `pop()`, `clear()`**
s = {1, 2, 3}
s.remove(1)     # Removes 1
# s.remove(10)  # ❌ Error if not present
s.pop()         # Removes random element
s.clear()       # Empties the set
print(s)        # set()


### ✅ 9. **`copy()`, `difference()`**
a = {1, 2, 3}
b = {3, 4, 5}
c = a.copy()
print(c)              # {1, 2, 3}
print(a.difference(b))# {1, 2}


### ✅ 10. **All Kinds of Set Operations (Symbols & Functions)**
#### Union
a = {1, 2}
b = {2, 3}
print(a | b)           # {1, 2, 3}
print(a.union(b))      # {1, 2, 3}

#### Intersection
print(a & b)           # {2}
print(a.intersection(b))  # {2}

#### Difference
print(a - b)           # {1}
print(a.difference(b)) # {1}

#### Symmetric Difference
print(a ^ b)                # {1, 3}
print(a.symmetric_difference(b))  # {1, 3}


### ✅ 11. **Frozenset Creation and Its Operations**
fs = frozenset([1, 2, 3])
# fs.add(4)  # ❌ Error: 'frozenset' object has no attribute 'add'
print(fs)

fs2 = frozenset([3, 4, 5])
print(fs | fs2)                # Union
print(fs & fs2)                # Intersection
print(fs - fs2)                # Difference
print(fs ^ fs2)                # Symmetric Difference
