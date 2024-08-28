a=int(input("Enter your 1st no:\n"))
b=int(input("Enter your 2nd no:\n"))
c=int(input("Enter your 3rd no:\n"))
print("The largest no:")
if a>b and a>c:
    print(a)
elif b>a and b>c:
    print(b)
else:
    print(c)