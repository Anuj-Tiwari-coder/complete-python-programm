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
for m in range(0,200):
    print(m)

for n in range(0,20, 4):
    print(n)

#while loop
i=0
while(i<100):
    print(i)
    i= i+10
# while loop wiyh else statement it eork whe the all condition will satisfy
j=100
while(j>0):
    print(j)
    j=j-10
else:
    print("i am done")