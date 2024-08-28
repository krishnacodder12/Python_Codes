#SINGLE INHERITENCE : ONE PARENT CLASS, ONE CHILD CLASS

#MULTILEVEL INHERITENCE : YOURSELF, PARENTS, GRANDPARENTS

#HIERARCHIAL INHERTIANCE - ONE PARENT CLASS, MANY CHILD CLASS

#MULTIPLE INHERITENCE - ONE CHILD,MANY PARENTS

#example of single inheritence
class Person(): #parent class, super class, base class
    def __init__(self,name,idno):
        self.name = name
        self.idno = idno

    def display(self):
        print(self.name,self.idno)
    
    def changeName(self,newName):
        self.name = newName
    
class Employee(Person): #child class, sub class, derived class
    def __init__(self,name,idno,sal,designation):
        super().__init__(name,idno) #to connect attributes of a parent class to child class
        self.sal = sal
        self.designation = designation

    def sample(self):
        print("Hello")

    #method overriding - modifying any existing function in the parent class
    def display(self):
        print(self.name,self.idno,)

obj2 = Person('Divya',345)
obj2.display()

obj = Employee('Sanjana',123,50000,'Teacher')
obj.sample()
obj.display()

    


