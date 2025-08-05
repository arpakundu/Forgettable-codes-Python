x = 3
print(id(x))

y = 3
print(id(x)) #For same value x and y will show exact same locations

y = 2
print(id(y)) #Here the location of y is changed because of the different value
