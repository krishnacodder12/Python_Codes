def add(a,b):
    print(a+b)


def sub(a,b):
    print(a-b)

def mul(a,b):
    print(a*b)

def div(a,b):
    print(a/b)

x=int(input("Enter your 1st no:\n"))
y=int(input("Enter your 1st no:\n"))
z=input("What you want to do")

if z=="+":
    add(x,y)
if z=="-":
    sub(x,y)

if z=="*":
    mul(x,y)

if z=="/":
    div(x,y)




