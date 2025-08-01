### ✅ 1. *Dictionary Creation*

#### 🔹 Empty Dictionary


d1 = {}
print(d1)  # {}


#### 🔹 Dictionary with Integer Keys


d2 = {1: 'apple', 2: 'banana'}
print(d2)  # {1: 'apple', 2: 'banana'}


#### 🔹 Dictionary with Mixed Keys


d3 = {'name': 'Alice', 10: [1, 2, 3]}
print(d3)  # {'name': 'Alice', 10: [1, 2, 3]}


#### 🔹 Create Empty Dictionary using dict()

d4 = dict()
print(d4)  # {}


#### 🔹 Creating Dictionary from List of Tuples

lst = [('a', 1), ('b', 2)]
d5 = dict(lst)
print(d5)  # {'a': 1, 'b': 2}



### ✅ 2. **Dictionary Access (get() and Others)**

d = {'x': 10, 'y': 20}
print(d['x'])        # 10
print(d.get('y'))    # 20
print(d.get('z', 0)) # 0 (default if key doesn't exist)



### ✅ 3. *Adding or Modifying Elements*

d = {'a': 1}
d['b'] = 2           # Add
d['a'] = 10          # Modify
print(d)             # {'a': 10, 'b': 2}




### ✅ 4. *Delete or Remove Element*

#### 🔹 pop()


d = {'a': 1, 'b': 2}
d.pop('a')           # Removes 'a'
print(d)             # {'b': 2}


#### 🔹 popitem() (removes last inserted)


d.popitem()
print(d)             # {}


#### 🔹 del


d = {'x': 1, 'y': 2}
del d['x']
print(d)             # {'y': 2}


#### 🔹 clear()


d.clear()
print(d)             # {}




### ✅ 5. *Dictionary Methods*

#### 🔹 copy()


d1 = {'a': 1}
d2 = d1.copy()
print(d2)  # {'a': 1}


#### 🔹 fromkeys()


keys = ['a', 'b', 'c']
d = dict.fromkeys(keys, 0)
print(d)  # {'a': 0, 'b': 0, 'c': 0}


#### 🔹 items(), keys(), values()

d = {'x': 100, 'y': 200}
print(d.items())   # dict_items([('x', 100), ('y', 200)])
print(d.keys())    # dict_keys(['x', 'y'])
print(d.values())  # dict_values([100, 200])


#### 🔹 dir() on dictionary


print(dir(d))  # Shows all attributes and methods of the dict




### ✅ 6. *Dictionary Comprehension*


squares = {x: x*x for x in range(1, 6)}
print(squares)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}




### ✅ *Additional Useful Methods and Tricks:*


### 1. **setdefault()**

#Used to get the value of a key and set a default if the key is missing.


d = {'a': 1}
d.setdefault('b', 100)  # Adds 'b' with value 100 if not present
print(d)  # {'a': 1, 'b': 100}




### 2. **update()**

#Used to merge another dictionary or key-value pairs.


d = {'x': 1}
d.update({'y': 2, 'z': 3})
print(d)  # {'x': 1, 'y': 2, 'z': 3}




### 3. *Looping through Dictionary*


d = {'a': 1, 'b': 2}
for k, v in d.items():
    print(k, v)




### 4. **Check Key Existence with in**

d = {'a': 1}
print('a' in d)     # True
print('b' not in d) # True




### 5. *Nested Dictionary Access*


student = {
    'name': 'Alex',
    'marks': {'math': 90, 'science': 85}
}
print(student['marks']['math'])  # 90




### 6. *Dictionary Length*


d = {'a': 1, 'b': 2}
print(len(d))  # 2




### 7. *Sorting a Dictionary (by keys or values)*


d = {'b': 2, 'a': 1, 'c': 3}
# By key
print(dict(sorted(d.items())))  
# By value
print(dict(sorted(d.items(), key=lambda x: x[1])))




### 8. *Merging Two Dicts (Python 3.9+)*

d1 = {'a': 1}
d2 = {'b': 2}
d3 = d1 | d2
print(d3)  # {'a': 1, 'b': 2}
