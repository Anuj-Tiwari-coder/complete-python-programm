
inpt = input("Enter an integer(between 5 and 9) : ")

try :
    if inpt == "quit":
        print("no error")

    elif 5 < int(inpt) < 9:
        print(f"{inpt}")

    elif int(inpt) < 5 or int(inpt) > 9:
        raise ValueError("Sahi value daal bhai")

except :
    print(f"please enter the either \"quit\" or the value between 5 and 9")

