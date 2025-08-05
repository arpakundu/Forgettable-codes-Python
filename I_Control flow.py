#control flow: if
num = 10
if num > 0:
    print("Number is positive")
print("This will always print")

if None:   # None , 0, False are cosidered as False 
    print("Number is positive")
print("This will always print")

#control flow: if ..else
num = -6
if num > 0:
    print("Number is positive")
else:
    print("Number is negative")

#control flow: if ..else
num = -6
if num > 0:
    print("Number is positive")
elif num == 0:
    print("Number is zero")
else:
    print("Number is negative")
    
#control flow: nested if
num = -6
if num >= 0:
    if num == 0:
        print("Number is zero")
    else:
        print("Number is positive")
else:
    print("Number is negative")


#control flow: while
#Find the product of all numbers present in the list
lst = [10, 20, 30, 40, 50]
product = 1
index = 0
while index<len(lst):
    product *= lst[index]
    index += 1
print("Product is {}".format(product))

#Find a number is prime or not
num = int(input("Enter a number: "))

if num < 2:
    print("Not prime")
else:
    i = 2
    is_prime = True  # Assume number is prime
    while i <= num // 2:
        if num % i == 0:
            is_prime = False  # Found a divisor, it's not prime
            break
        i += 1
    if is_prime:
        print("Prime number")
    else:
        print("Not prime")


#control flow: for
#Find the product of all numbers present in the list
lst = [10, 20, 30, 40, 50]
product = 1
for element in lst:
    product *= element
print("Product is {}".format(product))

#range() function
for i in range(10):
    print(i)
for i in range(1,10,2): #here 2 is the step size
    print(i)
for i in range(len(lst)):
    print(lst[i])
for i in lst:
    print(i)


#control flow: break & continue
lst = [10, 20, 30, 40, 50]
for element in lst:
    if element == 40:
        break
    print(element)
print("out of for loop")

#print odd numers of the list
lst = [1, 20, 3, 40, 55]
for element in lst:
    if element % 2 == 0:
        continue
    print(element)
else:
    print("out of for loop")


