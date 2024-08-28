def sum(a,b):
   print(a+b)

def sub(a,b):
    print(a-b)

def zero(a,b):
    print("zero")

def my_function(a,b):
    if a>0==0 and b>0==0:
        sum(a,b)
        
    elif a<0==0 and b<0==0:
        sub(a,b)
    else:
        zero(a,b)

x=int(input("Enter your 1st no:\n"))
y=int(input("Enter your 2nd no:\n"))
my_function(x,y)
