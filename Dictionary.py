#creating Dicatinary
dict={"Name": "Anuj",
      "Qualification": "Pyhton Dev",
      "Gratuation":"Bsc.cs"}


print("Dictionary:",dict, type(dict))

# This line shows none without the error
print(dict.get("Name1"))

print("Name:",dict["Name"])

print("Qualification:",dict["Qualification"])

print("Gratuation:",dict["Gratuation"])

print(dict.values())
print(dict.keys())
# for keys in dict.keys():
#     a=input("Enter your keys:")
#     if a in dict.keys():
#         print("Value of",a,"is",dict[a])
# else:
#     print("Not found")
# print(f"Dict keys and value{keys} is {dict[keys]}")

# print(dict.items())
# for keys, value in dict.items():
#     print(f"Dict keys and value {keys} is {value}")
# for b in dict:
#     b=input("Enter your key")
#     if b in dict.keys:
#         print("Value of",b,"is",dict[b])
#     else:
#         del dict
# Methods
dict.update({"age":21})
print(dict)
dict.pop("Qualification")
print(dict)
dict.popitem()
print(dict)
dict.clear()
print(dict)
# del dict
# print(dict)