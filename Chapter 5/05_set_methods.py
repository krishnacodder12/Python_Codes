# Creating an empty set
b=set()
print(type(b))

# Adding values to an empty set
b.add(4)
b.add(5)
#b.add([4, 5, 6])# We cannot use a list in sets adding method
# if we will use touple then only it will be add


b.add((4, 5, 6))
#b.add({4:5})#cannont use dictionary in adding method of sets
print(b)

#Length of the set
print(len(b))# Prints the length of the set

#remove of an item
b.remove(4)# remove 5 from set b
#b.remove(15)# throws an error while trying to remove 15 (which is not present in  the set)
print(b)

print(b.pop())
print(b)


