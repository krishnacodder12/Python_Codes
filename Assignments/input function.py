a=int(input("Enter the 1st no.:\n"))
b=int(input("Enter the 2nd no.:\n"))
c=int(input("Enter the 3rd no.:\n"))
sum=(a+b+c)
print("Sum of your no:", sum)

print("Average of your no:")
avg=(sum/3)
print(avg)

print("The largest no:")
if a>b and a>c:
    print(a)
elif b>a and b>c:
    print(b)
else:
    print(c)

print("The smallest no:")
if a<b and a<c:
    print(a)
elif b<a and b<c:
    print(b)
else:
    print(c)