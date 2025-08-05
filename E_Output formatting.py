#format() function
a = 10; b = 20
print("value of a is {} and value of b is {}".format(a,b))
print("value of a is {0} and value of b is {1}".format(a,b)) # here the index of a is 0 and index og b is 1
#using keywords argument to format the string
print("Hello {name}, {wish}".format(name="Arpa", wish="Congratulations!"))
#we can combine positional arguments with keyword arguments
print("The story of {0}, {1} and {other}".format("Arpa","Study",other="Peace"))

#Python input
#input() function
num = input("Enter a number: ")
print(num)
