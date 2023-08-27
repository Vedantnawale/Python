x =int(input("Enter the value of x : "))
match x:
    case 1:
        print("Value of x is 1")
    case 2:
        print("Value of x is 2")
    case 4:
        print("Value of x is 4")
    case _ if x!= 10:
        print("Value of x is not equal to 10")
    case _ if x!= 20:
        print("Value of x is not equal to 20")
    case _ if x!= 30:
        print("Value of x is not equal to 30")
    case _ :
        print("Default Value")