# Creating a tuple using ()
t=(1,2,3,4,5)

t1=() # Empty tuple
t1=(1)#Wrong way to declare a tuple with single element
t1=(1,)#Tuple with Single element (comma neecesary)
print (t1)

#Printing the element of tuple
#print(t[0])

#Cannot update the values of a tuple
t=(5,5,7,4,9)
t[0]=7 
print(t)