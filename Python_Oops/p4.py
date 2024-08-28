#constructor 2nd
#there are two types of cunstructor - 1> Parameterized constructor, 2> Default constructor 

class person:

    def __init__(self, n, o):
        print("Hey i am person")
        self.name = n
        self.occupation = o

    def info(self):
        print(f"{self.name} is a {self.occupation}")

a = person("Krishna", "Developer")
b = person("Ashutosh", "Tester")
a.info()
b.info()