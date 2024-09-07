Numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
list1 = list(Numbers)
list1.append(0)
list1.pop(3)
list1[2] = 0
tuple1 =tuple(list1) # convert list1 to a tuple
print("Numbers:", Numbers)
print("list is:", list1, "tuple is:", tuple1)
print(type(list1), type(tuple1))
res = list1.count(0)
print("there are 0 count:",res, "Here are previous tuple",list1 )
# if or else in tuple
if 2 in list1:
    print("present with indexcount:",res)
else:
    print("there are no index with 2")
