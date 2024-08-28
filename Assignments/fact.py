#factorial of even no.
a=int(input("Enter your no.:\n"))
fact=1
for i in range(1,a+1):
    if i%2==0:
        fact=fact*i
print(fact)