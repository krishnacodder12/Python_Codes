def factorial(a):
    fact=1
    for i in range(1,a+1):
        fact=fact*i
    print(fact)

b=int(input("enter your no:\n"))
factorial(b)

