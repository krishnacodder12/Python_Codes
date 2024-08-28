#ENCAPSULATION: Binding the data members and data functions just like a capsule.
#data members are kept private, give access in the function

class Base:
    def __init__(self) -> None:
        self.a = "VLA"
        self.__c = "Victory" #this is a private member

    def getAccesstoc(self):
        pwd = input("enter the pwd: ")
        if(pwd == "abc"):
            print(self.__c)
        else:
            print("You dont have access")

class Derived(Base):
    def __init__(self) -> None:
        super().__init__(self)
        print("Hello")
        print(self.__c)

obj = Base()
print(obj.a)
#print(obj.__c) #error will come bcuz we dont want the object to have access to a private member
obj.getAccesstoc()

obj2 = Derived()



#conclusion:
#a private data member is only accessible to its class. not even to its child class nor its object. Why? -> to avoid accessibility and modification to any sensitive data.
#but if u want to give access to any authorized user, u can do it by creating a function inside the base class and give access