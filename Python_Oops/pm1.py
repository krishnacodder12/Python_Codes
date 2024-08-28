class Student:
    def __init__(self,name,rollno,std,sec): #init is a constructor - special function
        self.name = name
        self.rollno = rollno
        self.std = std
        self.sec = sec

    def func(self):
        return "my name is : ",self.name,self.rollno
    
    def __str__(self): #to reperesent an object
        return f"hi I am a student object with {self.name} value"

#create an object
stu1 = Student("krishna",99,10,'a')
print(stu1)
#print(stu1.func())
#print(stu1.name)


