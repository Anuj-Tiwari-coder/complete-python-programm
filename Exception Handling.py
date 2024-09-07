# try and except
a=(input("Enter your number:"))
print(f"Multiplication of {a} is: ")
try:
    for x in range(1,11):
        print(f"table of {a}x{x}={int(a)*x}")
except Exception as e:
    print(e)
    print("Enter a valid number")
except ValueError:
    print("Enter a valid number")
except IndexError:
    print("Enter a valid number")

l=[1,2,3,4,5]
i=int(input("Enter the Index Number:"))
try:
    print(l[i])
except IndexError:
    print("Enter a valid index number")

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
    #  Finally is always executed
finally:
print("Thank you for using this program")
