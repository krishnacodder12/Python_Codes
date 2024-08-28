# Get Information through function
# self :- The self parameter is a refrence to the current instance 
# - of class and used to access variable that belongs to the class 
class person:
    name = "Krishna"
    occupation = "Web Developer"
    salary = 100000

    def info(self): #(self we can use when we create a function) 
        print(f"{self.name} is a {self.occupation}")
a = person()
b = person()
c = person()
a.name = "Kamlesh"
a.occupation = "App Developer"

b.name = "Rajesh"
b.occupation = "Python Devloper"

# print(a.name, a.occupation)
a.info()
b.info()
c.info() # basically in c we didn't put anything so it will print default value