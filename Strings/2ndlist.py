# find the sum of even no. in the list
print("Element for the list")
a=[]
for i in range(1,6):
    x=int(input("Enter your no:\n"))
    a.append(x)
fact=0
for i in a:
    if i%2==0:
        fact=fact+i
print(fact)