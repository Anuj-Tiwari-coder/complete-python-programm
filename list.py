# # # Creating List
Name=["Anuj", "AT", "Kailash"]
Mark=[8.1, 10, 6,3,5,7]
# print(len(Name))
# print(type(Name))
# print(len(Mark))
# print(type(Mark))
# print(Name[:])
# print(Mark[:])
# print(Mark[0:6:2]) # jumpcase
# if(input("enter your content:") in Name):
#         print("it is in the list")

# if ("AT" in Name):
#     print("it is in the list",[1])
# elif "Anuj" in Name:
#     print("it is in the list",[0])
# elif "Kailash" in Name:
#     print("it is in the list",[2])
# else:
#     print(Mark)

# # list comprehension
# lst=[ i*2 for i in range(12) [:11] if i*2]

# print(lst)

# Method in list
Name.append("Ario")
Mark.sort()
# Mark.sort(reverse=True)
Name.reverse
print(Name.count("Anuj"))
print(Name)
Name.insert(0, "AT"  )
Name.extend(Mark)
print(Name)
print(Mark.index(8.1))
print(Mark)
L=Mark
L[0]=1

print(L)
print(Mark+Name)
