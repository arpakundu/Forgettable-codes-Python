#Arithmatic Operators
x, y = 10, 20
print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x%y) #modulo
print(x//y) #Floor division
print(x**y) #exponent

#Comparision Operators
print(x>y)
print(x<y)
print(x==y)
print(x!=y)
print(x>=y)
print(x<=y)

#Logical operators
print(x and y)
print(x or y)
print(not x)

#Bitwise operators
print(x & y)
print(x | y)
print(~x)
print(x ^ y)
print(x >> y)
print(x << y)

# Assignment operators
x = 10
x += 10
print(x)

x -= 10
print(x)

x *= 10
print(x)

x /= 10
print(x)

x %= 10
print(x)

x = 10  # Resetting x for floor division
x //= 10
print(x)

x = 2  # Resetting x for exponentiation
x **= 3
print(x)

x = 5
x &= 3
print(x)

x = 5
x |= 3
print(x)

x = 5
x ^= 3
print(x)

x = 8
x >>= 2
print(x)

x = 2
x <<= 3
print(x)

#identity operators
a = 5
b = 5
c = 10
print(a is b)
print(a is not c)

# Membership operators
list1 = [1,2,3]
print(1 in list1)
