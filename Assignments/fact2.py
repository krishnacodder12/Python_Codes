a=int(input("Enter your no:\n"))
fact=0
for i in range(0,a+1):
    if i%2==0:
        fact=fact+i
print(fact)