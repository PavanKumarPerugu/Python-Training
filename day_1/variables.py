#1. Asigning Single variable
name = "Packing box" # A string
height = 10 # An integer assignment
width = 20.5 # A floating point

print (name)
print (height)
print (width)

#2. Asigning Multiple variables
#i
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

#ii
x = y = z = "Orange"
print(x)
print(y)
print(z)


"""

iii. Unpacking a collection. 
Works with Lists and Tupples. 
Dictionaries also can be unpacked but only the keys will be unpacked. 
Sets cqan be unpacked but we can't control the order to which variables they will be assigned to.

"""
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)


#iv. Global Variables
x = "awesome"
def myfunc():
  x = "fantastic"
  print("Python is " + x)
myfunc()
print("Python is " + x)