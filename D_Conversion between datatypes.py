float(5) #was iniitilly a int but now float
int(10.5) # was initially a float but now int
str(20) # was initially a int but now str
#('10p') # will give value error as 10 and p are two different datatype

# Concatination
user = "ARPA"
lines = 100
print("Congratuations! "+user+" you just completed "+str(lines)+" tasks of your TO-DO-LIST") #Here lines variable is int so we need to make it string first then concatinate it

a = [1, 8, 9]
print(type(a))
s = set(a) # converting list into set
print(s)
print(type(s))

l = list("Arpa") #converting string into list
print(l)
