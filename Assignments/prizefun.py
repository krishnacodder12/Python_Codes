def billing_fun(a,b):
    amt=a['Apple']*b[0]+ a['Banana']*b[1]+ a['Lahshun']*b[2]+ a['Mirch']*b[3] 
    print("your price is:\n", amt)

print("Available are: Apple,Banana,Lahshun,Mirch")
d={}
x=int(input("Enter no of items:\n"))
for i in range(0,x):
    item=input("Enter your item:\n ")
    quantity=int(input("Enter item quantity:\n"))
    d[item]=quantity

price=[20,60,40,90]
billing_fun(d,price)