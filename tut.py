import os
os.system("python --version")  

x = int(input("enter number"))
match x:
    case 1:
        print("number is 1")
    case 2:
        print("number is 2")
    case _:
        print("unknown")

        


