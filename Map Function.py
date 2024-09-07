# Map Fun is use for mapping the data and make easy to use for the def Fun

# for example
def cube(x):
    return x*x*x
print(cube(2))
l=[1,2,3,4,5]
newl=[]
for item in l:
    newl.append(cube(item))
print(newl,"\n")


# Except that we can also write like this
l=[11,2,3,4,5]
c= list(map(cube,l))
d= list(map(lambda x: x*x*x, l))
print("this code on map function",c,"\n")
print("this map fun is on lambda",d,"\n")

# Now Filter
# it is use for Filte the all types of data type:
filter_function= lambda x: x>3
f= list(filter(filter_function,l))
print("this is on filter function", f,"\n")

# Now reduce function
# for that you have to install funtools
from functools import reduce
Mysum= lambda x,y: x+y
numbers= [1,2,3,4,5,6,7,8,9]
s= reduce(Mysum,numbers)
print("this reduce function:",s)