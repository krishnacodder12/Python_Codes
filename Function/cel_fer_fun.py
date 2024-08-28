def temp(celcius):
    f=(celcius*(9/5))+32
    return f
    
b=int(input("Enter your temperature:\n"))
z=temp(b)
print(z)