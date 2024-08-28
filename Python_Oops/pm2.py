class Dog:
    def __init__(self,color) -> None:
        self.color = color

    def setColor(self,color):
        self.color = color
        print("color set successfully")

    def getColor(self): #user defined
        print(self.color)

    def bark(self):
        print("WOWOWOW")

class puppy:
    def __init__(self,color) -> None:
        self.color = color

    

   

dog1 = Dog("red") #object/instance
dog1.bark()
dog1.getColor()

color = input("enter new color: ")
dog1.setColor(color)

dog1.getColor()