def my_circle(r):#
    area=22/7*r*r
    print(area)

def my_square(s):
    square=s*s
    print(square)

def my_ractangle(l,b):#
    area=l*b
    print(area)

shape=input("Enter your shapes")
if shape=="circle":
    radius=int(input("Enter your radius"))
    my_circle(radius)

elif shape=="square":
    radius=int(input("Enter your side"))
    my_square(radius)

elif shape=="rectangle":
    length=int(input("Enter your length"))
    breath=int(input("Enter your breath"))
    my_ractangle(length,breath)
else:
    print("enter the correct shape")

