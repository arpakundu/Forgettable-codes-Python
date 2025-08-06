#######exception handling######
import sys
lst = ['b',0,2]
for entry in lst:
    try:
        print("the entry is: ",entry)
        r=1/int(entry)
    except:
        print("oops! ",sys.exc_info()[0]," occured")
        print("next entry")
        print("*")
print("the reciprocal of ",entry," is ",r)


###OTHER WAY
import sys
lst = ['b',0,2]
for entry in lst:
    try:
        print("*")
        print("the entry is: ",entry)
        r=1/int(entry)
    except(ValueError):
        print("This is valueerror")
    except(ZeroDivisionError):
        print("This is ZeroDivisionError")    
    except:
        print("Some other error")    
print("The reciprocal of ",entry," is ",r)


## manully user called error###
try:
    num = int(input("enter a positive number: "))
    if num <=0:
        raise ValueError("Entered negetive number")
    else:
        print("The entered positive number is: ",num)
except ValueError as e:
    print(e)


## no matter waht finally always get printed###
try:
    f = open('sample_text')
finally:
    f.close()
