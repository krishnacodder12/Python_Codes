#triangle means equal of 180
a=int(input("Enter your 1st triangle:"))
b=int(input("Enter your 2nd triangle:"))
c=int(input("Enter your 3rd triangle:"))
if a+b+c==180:
    print("it's triangle")
    if a==b and a==c:  #if inside if is called nested if
        print("it's equilateral")#
    elif a==b or a==c or b==c:
        print("it's isosceles")
    else:
        print("Scalane")
else:
    print("it's not triangle")