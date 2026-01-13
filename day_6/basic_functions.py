#1. Addition Function
print("\nAddition function")
def add(a, b):
    return f"Sum is {a + b}"

result = add(
    *map(int, input("Enter two integers separated by comma: ").split(','))
)
print(result)

#2. Default arguements
print("\nDefault arguements")
def greet(name, msg="Hello"): #msg is a default passing arguement
    print(msg, name)

greet("Pavan")
greet("Pavan", "Welcome")

#3. Scope (Local vs Global)
#i. Local variable
print("\nScope - Local variable")
def demo():
    x = 10  #local
    print(x)
demo()

#ii. Global variable
print("\nScope - Global variable")
x = 20
def demo():
    print(x)  #global
demo()

#iii. Global variable by defining with global keyword
print("\nScope - Global by defining with global keyword")
x = 5
def update():
    global x
    x = 10
update()
print(x)

'''#iv. Local vs Global variable
print("\nScope - Local vs Global variable")
def my_function():
    y = 20  # local variable
    print("Inside function, y =", y)
my_function()
print(y)  #This will cause an error: y is not defined outside'''

'''#v. Local vs Global variable
print("\nScope - Local vs Global variable")
counter = 0  #global variable
def increment():
    while counter<=10:
        counter += 1 #became local variable
        print("Inside function, counter =", counter)
increment()
print("\nOutside function, counter =", counter) #so as the counter is now a local variable, it throws an unboundlocal error'''

#vi. Local vs Global variable
print("\nScope - Local vs Global variable")
counter = 0  #global variable
def increment():
    global counter
    while counter<10:
        counter += 1 
        print("Inside function, counter =", counter)
increment()
print("\nOutside function, counter =", counter,"\n")

#vii. Local vs Global variable
print("\nScope - Local vs Global variable")
x = 5
def update():
    y = x
    return y
print(update())
x = 10
print(x)


#positional and keyword arguments
print("\nPositional and Keyword arguments")
def my_function(animal, name, age):
  print("I have a", age, "year old", animal, "named", name)
my_function("dog", name = "Buddy", age = 5)

#position only arguments
def my_function(name, /):
  print("Hello", name)
my_function("Emil")

#keyword only arguments
def my_function(*, name):
  print("Hello", name)
my_function(name = "Emil")

#Combining Positional-Only and Keyword-Only arguments
def my_function(a, b, /, *, c, d):
  return a + b + c + d
result = my_function(5, 10, c = 15, d = 20)
print(result)