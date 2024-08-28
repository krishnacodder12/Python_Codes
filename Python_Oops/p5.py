#Decorators
# *args is the source to get argument as a tuple
# **kwargs is the source to get argument as dictionary
# @greet is use to connect with another statement
def greet(fx):
  def mfx(*args, **kwargs): 
    print("Good Morning")
    fx(*args, **kwargs)
    print("Thanks for using this function")
  return mfx

@greet
def hello():
  print("Hello world")

@greet
def add(a, b):
  print(a+b)
  
# greet(hello)()
hello()
# greet(add)(1, 2)
add(1, 2)
