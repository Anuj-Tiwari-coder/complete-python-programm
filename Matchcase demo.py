a=(int(input(("enter your number:"))))
match a:
    case 1:
        print("value of a:",20)
    case 2:
        print("valuue of a",a)
    #case with if condition
    case _ if a<=10:
        print("null")