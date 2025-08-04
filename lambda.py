double = lambda x:x*2
print(double(5))

#################
lst1=[1,2,3,4,5,6]
even_lst= list(filter(lambda x: (x%2==0), lst1))
print(even_lst)

######################
lst2=[1,2,3,4,5,6]
new_lst=list(map(lambda x: x**2, lst2))
print(new_lst)

######################
from functools import reduce
lst3=[1,2,3,4,5,6]
product_lst=reduce(lambda x,y: x*y, lst3)
print(product_lst)

######################
