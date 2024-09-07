import os
print("heloo word from....")
os.system("python version")

# Display print value
print("hello World")


# integers not need double Qutes
print(5)

# basic math and 2 more floor devision and reminder
print(12+23, 12-23, 12*23, 12/23, (2.3 ,"is a float value"))
print(12//23, 23%12)
# use new line
print("12 \n23")

# using sepraters symbol
print("combine with different char",  2, 4, sep="-")
# variables in a container
# Data type for variables(same type needed to Concatenate)
a = "hello"
b = 12345678910
c = True    # without double quotes called Boolean
d = 10987654321
e = "world"
f = 2.3
print(a)
print(b)
print(c)
print(a+e) # Concatenation

# For identify the data type
print("type of data ",type(a))
print("type of data ",type(b))
print("type of data ",type(c))
print("type of data ",type(d))
print("type of data ",type(e))
print("type of data ",type(f))

# Creating A list and tuple both are use for array
list =[[1,2,3,4,5],["a", "b","c","d","e"]]
print(list)
tuple=(1,2,3,4,5)
print(tuple)
# Dictionary
dict ={"name":"Sanatan", "own by": "Sanatani's", "age": "Aproxmatily 5000 years", "work as": "Devotees"}
print(dict)

# typeCasting string becaming integer but using int function
a="30"
b="43"
c=30
d=43
print((int(a)+int(b)), a+b)
# typeCasting integer becoming string but using str function
print(str(c),str(d))
# there are tow type implicit and explicit

# perform input funtion
a=str(input("give input:"))
b=str(input("give input:"))
print( "concatination:",a+b)
x=int(input("enter first number="))
y=int(input("enter second number="))
print(x+y)

#Multiple lines in string
str="Hello , World"
lines="""
hello
world
from python!!!!!!"""
print (str+lines)

#indexing string and like that we can also index the array of charaters
print(str[0])
print(lines[1],"\n")

#lets use a loop
#for loop
#Be careful on indentation
for  charater in lines:
    print("for indexing hole charater in one time:", charater)
print(str[0:5])

#length of string array
print("length of character in str:",len(str))

#-ive silicing
print("length of character in str in -ive:",str[:-3])

# methods in string
print(str.upper())
print(lines.lower())
print()
print(lines.rstrip("!"))
print(lines.replace("hello", "hii"),"\n")
print(str.capitalize())
print(lines.endswith("!"))
print(str.startswith("Hello"))
print(str.count("h"))
print((len(str.center(50))))
print(str.find("Hello"))

# index use for end the program if the values are not found
#print(str.index("aaa"))
#print(str.isalnum())
#print(lines.isalpha())
print(lines.islower())
print(str.isupper())
print(str.isprintable())
print(lines.isspace())
print(str.istitle())

#looping methods: 
#conditional operators: "<, >, <=, =>, ==, !="
a=int(input("enter your no"))
print(a<18)
print(a>18)
print(a<=18)
print(a!=18)
print(a==18)

#if_else method
a=int(input("enter your no"))
if(a>18):
    print("your are eligible")
else:
    print("you'r not eligible")

#if-elif
num1=int(input("enter your number"))
num2=int(input("enter yor number"))
if(num1>num2):
    print("value", num1+num2)
elif(num1<=num2):
    print("value 2",num2-num1)
else:
    print("none:")

#Matchcase = switch cases
a=(int(input(("enter your number:"))))
match a:
    case 1:
        print("value of a:",20)
    case 2:
        print("valuue of a",a)
    #case with if condition
    case _ if a<=10:
        print("null")

#looping methods:
#if_else method
a=int(input("enter your no"))
if(a>18):
    print("your are eligible")
else:
    print("you'r not eligible")

#if-elif
num1=int(input("enter your number"))
num2=int(input("enter yor number"))
if(num1>num2):
    print("value 1:", num1+num2)
elif(num1<=num2, num1==1):
    print("value 2:",num2-num1)
else:
    print("none:")
    
# one line if... else condition
a=input("enter Anything: ")
b=input("Enter Anything: ")
print("A") if a==b else print("B") 


#for loop
Name=input("enter yor name")
x=Name
for i in Name:
    print(i, end=",")
    
#if-else in for loop
if (i==x):
    print("Name:", Name)
else:
    print("null")

#range function
for m in range(0,2000):
    print(m)

for n in range(0,20, 4):
    print(n)
#while loop
i=0
while(i<100):
    print(i)
    i= i+10
print("done")
# while loop wiyh else statement it eork whe the all condition will satisfy
j=100
while(j>0):
    print(j)
    j=j-10
else:
    print("i am done")
# break statment
i=int(input("enter your num:"))
j=i
for i in range(11):
    print(j,"X", i+0, "=", i*j)
    if(i==10):
        break
    continue
print(i==11)

i=0
while(i<100):
    print(i)
    i= i+10
print("done")

j=100
while(j>0):
    print(j)
    j=j-10
print ("while done")

# Creating Finction:
def your_name(a1,a2):
    variable=(a1,a2)
def your_age(c):
    int=(c)
a1=("hello")
a2=input("Enter your Name:")
your_name(a1,a2)
print("your Name:",a2)
print(a1,a2)

c=int(input("Enter your Age:"))
print("your age:",c)
your_age(c)
if c>18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")

# Creating List
Name=["Anuj", "AT", "Kailash"]
Mark=[8.1, 10, 6,3,5,7]
print(len(Name))
print(type(Name))
print(len(Mark))
print(type(Mark))
print(Name[:])
print(Mark[:])
print(Mark[0:6:2]) # jumpcase
if(input("enter your content:") in Name):
        print("it is in the list")

# if ("AT" in Name):
#     print("it is in the list",[1])
# elif "Anuj" in Name:
#     print("it is in the list",[0])
# elif "Kailash" in Name:
#     print("it is in the list",[2])
else:
    print(Mark) 

# list comprehension
lst=[ i*2 for i in range(12) [:11] if i*2] 
print(lst)

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
# count()
# index()
# len()
# max()
# min()
# Tuples are immutable
# Tuples are faster than list

# Recursion
# by Factorial
def factorial(n):
    if n == 1 or n==1:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(5))
# we can Also take as like this
# Factorial(5)
# 5 * Factorial(4)
# Factorial(4)
# 4 * Factorial(3)
# Factorial(3)
# 3 * Factorial(2)
# by Fibonacci series
# formula = F(0) = 0(1), F(1)= 1(1)
def fibonacci(n):
    a, b = 0, 1
    result = []
    for i in range(n):
        result.append(a)
        a, b = b, a + b
    return result

print(fibonacci(10))  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]# def fibonacci(n):

# creating set
# set does not consider the repeated value
s={1,2,3,4,5,6,7,8,9,0,1,4,5}
print(s)
# set cannot be empty if it's empty then is type show as a dict
s={}
print(type(s))
if (type(s)!=set):
    print("set is empty")
else:
    print("set is not empty")
s={1,2,2,3}
print(type(s))
if (type(s)==set):
    print("s is set")
else:
    print("s is not set")

# Methods for sets
s1={1,2,3,4,5,2,3,4,5}
print(s,s1)
print(s.union(s1))
s1.update(s)
s3=s1.intersection(s)
print(s3)
s3.intersection_update(s1)
s1.difference_update(s)
print(s)
s1.symmetric_difference_update(s)
print(s1)
s1.remove(1)
print(s1)
s1.discard(1)
print(s1)
s1.pop()
print(s1)
s1.clear()
print(s1)
print(s3.isdisjoint(s))
print(s3.issubset(s))
print(s3.issuperset(s))
print(s3.copy())
print(s3)

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
del dict
print(dict)

# try and except
a=(input("Enter your number:"))
print(f"Multiplication of {a} is: ")
try:
    for x in range(1,11):
        print(f"table of {a}x{x}={int(a)*x}")
except Exception as e:
    print(e)
    pass

# # try and except
# a=(input("Enter your number:"))
# print(f"Multiplication of {a} is: ")
# try:
#     for x in range(1,11):
#         print(f"table of {a}x{x}={int(a)*x}")
# except Exception as e:
#     print(e)
#     print("Enter a valid number")
# except ValueError:
#     print("Enter a valid number")
# except IndexError:
#     print("Enter a valid number")

# l=[1,2,3,4,5]
# i=int(input("Enter the Index Number:"))
# try:
#     print(l[i])
# except IndexError:
#     print("Enter a valid index number")

# Raise error method use for custom Error
a=int(input("Enter the value between 5 to 9: "))
b=input("quit")
if a<5 or a==9 :
    raise ValueError("Enter a valid number")
elif b=="quit":
    print("end the program")
    breakpoint
else:
    print("Fullfil the given condition")
    # # Finally is always executed
# finally:
#     print("Thank you for using this program")

# one line if... else condition
a=input("enter Anything: ")
b=input("Enter Anything: ")
print("A") if a==b else print("B") 

# those object out of the function it's called Global Variable
# Those are inside the functin that value is called Local variable

g= 5 # this is a global variable
print(f"this is Global {g} Variable ")
# use global
def local():
    h= 4
    global x
    x=3
    print(f"this is local {h} Variable")
    print(f"this is after Modify {x} global value")
local()
# we can access the function for Global but can't use local

# lambda function is use to make a one line def function
# use this when a anonynomus expression want to give for a short period of time
# we can also pass the fun with fun
# it is also use as temporary function

# Example
def avg(x):
    return x*2

print(avg(2))

# now Lambda Fun
sum= lambda X: X+4
cube= lambda X: X*X*X
multiply= lambda X:X*X
div= lambda X: X/X
print(sum(2))
print(cube(2))
print(multiply(2))
print(div(4),"\n")

avg= lambda X,y: (X+y) /2
print("avg",avg(1,2))

def fun(fx, value):
    return 6+ fx(value)
print(fun(multiply,3))

# lambda fun use at when we make more then 3 func in one program

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
from functools import reduce
Mysum= lambda x,y: x+y
numbers= [1,2,3,4,5,6,7,8,9]
s= reduce(Mysum,numbers)
print("this reduce function:",s)

# is key is use as equal object , same as == operator
a= "this is a"
b= "this is b"

print("this is (== operators): ",{a==b}) # exact location of object in memory
print("this is (is keyword): ",{a is b}) # exact location of object in memory
print(a,":", {a is a})
print(b ,":",{b == b})

