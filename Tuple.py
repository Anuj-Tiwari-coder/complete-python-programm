# Creating Tuple and tuple is constant
T=(1,2,3,)
t=(1,)
print(len(T), len(t))
print(type(T), type(t),T,t)
print(t[0])
print(T[0])
# loop in tuple
if 2 in T:
    print("yes it is present", T[1])
else:
    print("not present")
if 2 in t:
    print("yes it is present")
else:
    print("not present", "only:", t ,"is present")
# slicing Method in that it will created new tuple
T1= T[1:]
print(T1)

# Tuple Methods
Numbers=(1,2,3,4,5,6,7,8,9,)
list=list(Numbers)
list.append(0)
list.pop(3)
list[2]= 0
Numbers=tuple(list)
print("list is:",list,
    "Numberis:",Numbers)
print(type(list),type(Numbers))
# count()
res = list.count(0)
print("there are 0 count:",res, "Here are previous tuple",list )
# len()
print("len of list:",len(list))
# index()
res=list.index(2)
print(res,type(res))
# max()
# min()
# Tuples are immutable
