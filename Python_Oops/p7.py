# inheritance - when a class drives from another class
#Types - 1. Single Inh, 2.Multiple inh, 3. multilevel inh, 4. hierarchical inh, 5. hybrid inh

class employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def showdetails(self):
        print(f"The name of employee: {self.id} is {self.name}")

class programmer(employee):
    def showlanguage(self):
        print("The default language is python")

e1 = employee("Krishna", 3105)
e1.showdetails()

e2 = programmer("Kamlesh", 3106)
e2.showlanguage()