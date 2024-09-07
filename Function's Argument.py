def average(a=21, b=9):
    print("Your average is:" , a+b/100)
average(a=21)
average(b=9)
average(a=21, b=9)

def Details(Name, Age, Hobby):
    print("Your given Details:", Name , Hobby, Age)

Details(Name=input("Enter your Name:"),
        Age=int(input("Enter your age")),
        Hobby=input("Enter your Hobby"))
print(Details)