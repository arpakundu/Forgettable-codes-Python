### 1. *Function Arguments (Positional Arguments)*

def greet(name):
    print("Hello", name)

greet("Alice")  # Output: Hello Alice

### 2. *Default Arguments*

def greet(name="Guest"):
    print("Hello", name)

greet()         # Output: Hello Guest
greet("Bob")    # Output: Hello Bob

### 3. *Keyword Arguments*

def greet(name, msg):
    print(msg, name)

greet(name="Alice", msg="Hi")  # Output: Hi Alice

### 4. **Arbitrary Arguments (*args)**

def add(*nums):
    print(sum(nums))

add(1, 2, 3)  # Output: 6

### 5. **Arbitrary Keyword Arguments (**kwargs)**

def info(**details):
    print(details)

info(name="Alice", age=25)  # Output: {'name': 'Alice', 'age': 25}
