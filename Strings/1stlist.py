#
print("Enter the elements for the list")
a=[]
for i in range(1,6):
    x=int(input('enter the number : '))
    a.append(x)
fact=1
for i in a:
    if i%2==0:
        fact=fact*i
print(fact)


