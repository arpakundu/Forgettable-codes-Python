#Numbers
#type() function
a = 5
print(a," is a type of ",type(a))
#isinstance()function
#Checking the type is or not
b = 1 + 2j
print(b, " is a complex number?")
print(isinstance(1 + 2j, complex))

#Boolean
x = True
y = False
print(type(x))
print(type(y))

#String
s = "My name is AK"
s1 = 'My title is kundu'
s2 = '''My comfort food is homemade food''' #we can write string in this 3 ways
print(type(s))
print(type(s1))
print(type(s2))

s3 = '''CSE Specialization in
        AI & ML'''
s4 = """CSE Specialization in
        AI & ML"""              #Multiline string can be written like this
print(type(s3))
print(type(s4))
# Index value
print(s[0]) 
#Length of string ->> len() function
print(len(s))
#Slicing the string
print(s[:5]) #String from 0 to 4
print(s[5:10]) # String from 5 to 9

#List(Lists are ordered, mutable)
l = [10, 20.5, "Hello"]
print(l)
#print index value
print(l[0])
#changing the value of an index
l[2] = "Hola"
print(l)

#Tuple(they are ordered, immutable)
t = (10, 20.4, "AI&ML")
print(t)
#printing the value of index
print(t[1])
#t[1] = 20.5  #XXXXXXXXX can't be done will throw error XXXXXXXXX
#print(t)
#changing the value of any index in a tuple is not alllowed 

#Sets(they are unordered, collection of unique items)
se = {10, 20, 50, 80, 5}
print(type(se))
se1 = {10, 80, 90, 10}
print(se1) # set dont allow duplicate value so it will print 10 only once
#print(se[1]) #set doesn't suport indexing as they are unordered

#Dictionary
di = {'a':'apple','b':'bowl'}
di1 = {"a":"apple","b":"bowl"} #both written way are correct
print(di)
print(type(di))
print(di['a']) #printing the value of key 'a'
