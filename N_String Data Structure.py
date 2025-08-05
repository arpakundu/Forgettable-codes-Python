## ✅ 1. *String Creation*


s1 = "Hello"
s2 = 'World'
s3 = """Multiline
String"""
print(s1, s2, s3)



## ✅ 2. *Accessing Characters*


s = "Python"
print(s[0])    # P
print(s[-1])   # n



## ✅ 3. *Slicing a String*

s = "Programming"
print(s[0:6])   # Progra
print(s[:4])    # Prog
print(s[4:])    # ramming
print(s[::-1])  # gnimmargorP (reversed)




## ✅ 4. *String Immutability*


s = "hello"
# s[0] = 'H'  # ❌ Error: strings are immutable




## ✅ 5. *Concatenation and Repetition*


s1 = "Hello"
s2 = "World"
print(s1 + " " + s2)  # Hello World
print(s1 * 3)         # HelloHelloHello




## ✅ 6. *Membership Testing*


s = "banana"
print("a" in s)       # True
print("x" not in s)   # True




## ✅ 7. *String Comparison*


print("apple" == "Apple")   # False (case-sensitive)
print("a" < "b")            # True (lexicographic order)




## ✅ 8. *Looping Through a String*


for char in "dog":
    print(char)




## ✅ 9. *String Formatting*

#### 🔹 f-string


name = "Alex"
print(f"Hello, {name}!")


#### 🔹 format()


print("Welcome, {}".format("Sam"))


#### 🔹 % formatting


print("My age is %d" % 25)




## ✅ 10. *String Built-in Methods (with Examples)*

### 🔹 Case Conversion


s = "hello world"
print(s.upper())       # HELLO WORLD
print(s.lower())       # hello world
print(s.capitalize())  # Hello world
print(s.title())       # Hello World
print(s.swapcase())    # HELLO WORLD → hello world




### 🔹 Search & Replace


s = "banana"
print(s.find("na"))      # 2
print(s.rfind("na"))     # 4
print(s.index("a"))      # 1
print(s.replace("na", "NA"))  # baNANA




### 🔹 Check Start/End


s = "hello"
print(s.startswith("he"))  # True
print(s.endswith("lo"))    # True




### 🔹 Count Occurrences


s = "banana"
print(s.count("a"))    # 3




### 🔹 isX Methods (Check string types)


print("abc".isalpha())     # True
print("123".isdigit())     # True
print("abc123".isalnum())  # True
print("HELLO".isupper())   # True
print("   ".isspace())     # True
print("title Case".istitle())  # True




### 🔹 Strip / Remove Whitespace


s = "   hello   "
print(s.strip())    # 'hello'
print(s.lstrip())   # 'hello   '
print(s.rstrip())   # '   hello'




### 🔹 Join & Split


words = ["Python", "is", "fun"]
print(" ".join(words))     # Python is fun

s = "apple,banana,mango"
print(s.split(","))        # ['apple', 'banana', 'mango']




### 🔹 Partition and Splitlines


s = "name=John"
print(s.partition("="))   # ('name', '=', 'John')

multiline = "line1\nline2\nline3"
print(multiline.splitlines())  # ['line1', 'line2', 'line3']




### 🔹 Encoding / Decoding


s = "hello"
encoded = s.encode()
print(encoded)           # b'hello'
print(encoded.decode())  # hello




### 🔹 zfill(), rjust(), ljust()


print("7".zfill(3))     # 007
print("hi".rjust(5))    # '   hi'
print("hi".ljust(5, "*"))  # 'hi***'



## ✅ 11. *Escape Characters*


print("He said \"Hello\"")  # He said "Hello"
print("Line1\nLine2")




## ✅ 12. *Raw String*


path = r"C:\new\text"
print(path)  # C:\new\text (no escape)




## ✅ 13. *String Length*


s = "hello"
print(len(s))  # 5



## ✅ Summary of Most Used Methods (Quick View)

# | Category | Methods/Operations                              |
# | -------- | ----------------------------------------------- |
# | Creation | "text", 'text', """multi"""               |
# | Access   | [], slicing, in, loops                      |
# | Format   | f"", format(), %                          |
# | Case     | upper(), lower(), capitalize(), title() |
# | Test     | isalpha(), isdigit(), isalnum() etc.      |
# | Modify   | replace(), strip(), join(), split()     |
# | Search   | find(), index(), startswith(), count()  |
# | Encoding | encode(), decode()                          |
# | Padding  | zfill(), rjust(), ljust()                 |
# | Other    | partition(), splitlines(), len()          |

