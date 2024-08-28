myDict = {
    "Slow" : "in a good manner",
    "Krishna" : "A coder",
    "Marks" : [1,2,3,4,5],
    "anotherDict" : {'Slow': 'hero'}
}
#Dictionary method
print(myDict.keys())#print the key of the Dictionary
print(myDict.values())# print the values of the Dictionary
print(myDict.items())# print the (key,value) for all content of the Dictionary
print(myDict)
updateDict = {
    "Kamlesh" : "Besty"
}
myDict.update(updateDict)#Updates the dictionary by adding key value pairs from updatedict
print(myDict)
print(myDict.get("Kamlesh2"))# Returns none as Kamlesh2 is not present in the dictionary
print(myDict['Kamlesh2'])# throws an error as Kamlesh2 is not present in the dictionary