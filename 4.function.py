#function
from unicodedata import name


print("here is example function")

def who_am_i(): #this is a function
  name = "bloodyh"
  age = 30
  print("my name is " + name + "and i am " + str(age) + " year old")

who_am_i()
print("\n")

def add_one_hun(num):
		print(num+100)
		
add_one_hun(50)

#multiple parameters
def add(x,y):
	print(x + y)
add(10,7)

def multiply(x,y):
		return x * y
print(multiply(7,7))

def square_root(x):
		print(x ** .5)
square_root(64)

def nl():
	print('\n')
nl()