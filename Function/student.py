def fee_payment(level):
    if level==1:
        b=input("Enter your UPI ID:\n")
        c=input("Enter your password:\n")
        print("Transaction successfully done")
    elif level==2:
        b=input("Enter your UPI ID:\n")
        c=input("Enter your password:\n")
        print("Transaction successfully done")
    
    elif level==3:
        b=input("Enter your UPI ID:\n")
        c=input("Enter your password:\n")
        print("Transaction successfully done")

def math():
    print("Thank you for choosing math")
    a=int(input("Enter your level"))
    if a==1:
        print("Your fees is 500. do you want to continue to reg")
    elif a==2:
        print("You fees is 1000. do you want to continue to reg")
    elif a==3:
        print("You fees is 1500. do you want to continue to reg")

    ch = input("enter ur choice")
    if ch=="yes":
        fee_payment(a)
    else:
        print("Thank You")


        
    
   

a=input("Enter your name:\n")
b=int(input("Enter your mob no:\n"))
c=input("Enetr your course")

if c=="math":
    math()

elif c=="phy":
    math()

elif c=="chem":
    math()
    