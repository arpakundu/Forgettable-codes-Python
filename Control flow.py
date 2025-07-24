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
