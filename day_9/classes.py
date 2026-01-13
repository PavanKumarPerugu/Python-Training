'''
🧠 Concepts (3 hours)
1. Classes and Objects (45 min)

Goal: Understand how to define classes and create objects.
Topics:

What is a class?

What is an object?

Syntax of defining a class

Creating object instances

Accessing attributes and methods using the . operator

Example:

'''

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

car1 = Car("Toyota", "Corolla")
print(car1.brand)
print(car1.model)

'''
2. Attributes (30 min)

Goal: Learn about instance and class attributes.
Topics:

Instance attributes → specific to each object

Class attributes → shared by all objects

Example:

'''

class Dog:
    species = "Canine"  # class attribute

    def __init__(self, name):
        self.name = name  # instance attribute

dog1 = Dog("Buddy")
print(dog1.name, dog1.species)


'''
3. Methods (30 min)

Goal: Learn to define behaviors inside classes.
Topics:

Instance methods

Class methods (@classmethod)

Static methods (@staticmethod)

Example:

'''

class Calculator:
    def add(self, a, b):
        return a + b

    @staticmethod
    def info():
        print("This is a static method")

calc = Calculator()
print(calc.add(3, 5))
Calculator.info()
calc.info()


'''
4. The __init__ Method (30 min)

Goal: Understand object initialization and constructors.
Example:

'''

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Alice", 25)
print(p1.name, p1.age)


'''
5. Object Lifecycle (15 min)

Goal: Learn creation, usage, and deletion of objects.
Topics:

__init__() → constructor

__del__() → destructor

Example:

'''

class Example:
    def __init__(self):
        print("Object created")

    def __del__(self):
        print("Object deleted")

obj = Example()
del obj

'''
6. Inheritance (30 min)

Goal: Learn how child classes inherit properties and methods.
Topics:

Base and derived classes

Overriding methods

super() keyword

Example:

'''

class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

dog = Dog()
dog.speak()


# 5 small class examples


'''
🏎️ 1. Car Class

Concepts Covered: Constructor, instance attributes, method for display.

'''

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def start_engine(self):
        print(f"The {self.brand} {self.model} engine has started!")

# Object
car1 = Car("Tesla", "Model 3", 2024)
car1.start_engine()
print(f"Car Info: {car1.brand}, {car1.model}, {car1.year}")


'''
🎓 2. Student Class

Concepts Covered: Attributes, methods for calculating grades.

'''

class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks  # out of 100

    def check_result(self):
        if self.marks >= 50:
            print(f"{self.name} passed with {self.marks}% marks.")
        else:
            print(f"{self.name} failed with {self.marks}% marks.")

# Object
s1 = Student("Pavan", 101, 82)
s1.check_result()
print(f"Student Info: Name = {s1.name}, Roll No = {s1.roll_no}")


'''
📚 3. Book Class

Concepts Covered: Object attributes, string formatting, simple display method.

'''

class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display_info(self):
        print(f"'{self.title}' by {self.author} costs ₹{self.price}")

# Object
b1 = Book("Atomic Habits", "James Clear", 499)
b1.display_info()
print(f"Book Title: {b1.title}")


'''
💻 4. Laptop Class

Concepts Covered: Default attribute values, custom methods.

'''

class Laptop:
    def __init__(self, brand, ram, storage):
        self.brand = brand
        self.ram = ram
        self.storage = storage
        self.is_on = False

    def power_on(self):
        self.is_on = True
        print(f"{self.brand} laptop is now ON.")

# Object
l1 = Laptop("HP", "16GB", "512GB SSD")
l1.power_on()
print(f"Laptop Details: {l1.brand}, {l1.ram}, {l1.storage}")


'''
🧍 5. Employee Class

Concepts Covered: Instance method with computation, formatted output.

'''

class Employee:
    def __init__(self, name, salary, position):
        self.name = name
        self.salary = salary
        self.position = position

    def yearly_bonus(self):
        bonus = self.salary * 0.1
        print(f"{self.name} ({self.position}) gets a yearly bonus of ₹{bonus:.2f}")

# Object
e1 = Employee("Anita", 60000, "Manager")
e1.yearly_bonus()
print(f"Employee: {e1.name}, Salary: ₹{e1.salary}")


'''
2. Shape Classes

Goal: Demonstrate inheritance and method overriding.
Example:

'''

import math

class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

c = Circle(5)
r = Rectangle(4, 6)
print("Circle Area:", c.area())
print("Rectangle Area:", r.area())


'''
4. Bank Account Class

Goal: Include deposit, withdraw, and balance check methods.
Example:

'''

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ₹{amount}. New balance: ₹{self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ₹{amount}. Remaining balance: ₹{self.balance}")
        else:
            print("Insufficient balance!")

account = BankAccount("Pavan", 1000)
account.deposit(500)
account.withdraw(300)