'''
🧩 1. Instance Attributes
✅ Definition:

Attributes (variables) that belong to a specific object (instance) of a class.

Defined inside the __init__() method using self.

Each object has its own copy of these attributes.

💡 Key Point:

Changing s1.marks won’t affect s2.marks.

📘 Example:

'''

class Student:
    def __init__(self, name, marks):
        self.name = name          # instance attribute
        self.marks = marks        # instance attribute

s1 = Student("Pavan", 85)
s2 = Student("Anita", 92)

print(s1.name, s1.marks)  # Pavan 85
print(s2.name, s2.marks)  # Anita 92


'''
🏛️ 2. Class Attributes
✅ Definition:

Attributes that are shared by all instances of a class.

Defined outside methods, directly under the class.

💡 Key Point:

Class attributes are shared memory.

Instance attributes are unique memory.

📘 Example:

'''

class Student:
    school = "ABC High School"  # class attribute (shared)

    def __init__(self, name):
        self.name = name        # instance attribute

s1 = Student("Pavan")
s2 = Student("Anita")

print(s1.school)  # ABC High School
print(s2.school)  # ABC High School

# If you modify it through class, it changes for all
Student.school = "XYZ International"
print(s1.school, s2.school)  # both now see XYZ International


'''
⚙️ 3. Instance Methods
✅ Definition:

Regular methods that work on individual objects.

Require self as the first parameter.

Can access both instance and class attributes.

📘 Example:

'''

class Employee:
    company = "TechCorp"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show_info(self):  # instance method
        print(f"{self.name} works at {Employee.company} and earns ₹{self.salary}")

e1 = Employee("John", 50000)
e1.show_info()


'''
🏷️ 4. Class Methods
✅ Definition:

Methods that act on the class itself, not on specific objects.

Defined using the @classmethod decorator.

The first parameter is cls, representing the class.

💡 Key Point:

Use class methods to modify class-level data.

They can be called using either the class name or an object.

📘 Example:

'''

class Employee:
    company = "TechCorp"

    @classmethod
    def change_company(cls, new_name):
        cls.company = new_name

# Call without creating an object
Employee.change_company("NextGen Solutions")
print(Employee.company)  # NextGen Solutions


'''
🔧 5. Static Methods

✅ Definition:

Methods that do not depend on class or instance data.

Defined using the @staticmethod decorator.

Don’t take self or cls as parameters.

Used for utility/helper functions related to the class.

💡 Key Point:

Use static methods when logic is related to the class but doesn’t need its data.

📘 Example:

'''

class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

print(MathUtils.add(5, 7))  # 12


'''

🧱 6. Abstract Methods

✅ Definition:

Methods that are declared but not implemented in the base class.

Used when you want subclasses to implement the method in their own way.

Created using the abc (Abstract Base Class) module.

💡 Key Point:

You cannot instantiate a class that has abstract methods.

Used to enforce a contract: every subclass must implement certain methods.

📘 Example:

'''

from abc import ABC, abstractmethod

class Shape(ABC):  # Abstract base class
    @abstractmethod
    def area(self):
        pass  # no implementation here

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

c = Circle(5)
print(c.area())  # 78.5


'''
🔄 7. Quick Comparison Table
| Type                   | Keyword / Decorator | Belongs To | Access To            | First Param        | Common Use                             |
| ---------------------- | ------------------- | ---------- | -------------------- | ------------------ | -------------------------------------- |
| **Instance Attribute** | –                   | Object     | Specific object      | `self`             | Data unique to each object             |
| **Class Attribute**    | –                   | Class      | Shared by all        | `cls` (in methods) | Common data for all objects            |
| **Instance Method**    | –                   | Object     | Instance & Class     | `self`             | Behavior tied to object                |
| **Class Method**       | `@classmethod`      | Class      | Class (not instance) | `cls`              | Modify class-level data                |
| **Static Method**      | `@staticmethod`     | Class      | None (no self/cls)   | –                  | Utility or helper methods              |
| **Abstract Method**    | `@abstractmethod`   | Base Class | Must be overridden   | `self`             | Enforce method structure in subclasses |
'''

'''
🧩 Example Combining All Concepts

'''

from abc import ABC, abstractmethod

class Employee(ABC):
    company = "TechCorp"  # class attribute

    def __init__(self, name, salary):
        self.name = name      # instance attribute
        self.salary = salary

    def show_info(self):       # instance method
        print(f"{self.name} earns ₹{self.salary} at {Employee.company}")

    @classmethod
    def change_company(cls, new_name):  # class method
        cls.company = new_name

    @staticmethod
    def company_policy():  # static method
        print("All employees must complete safety training.")

    @abstractmethod
    def calculate_bonus(self):  # abstract method
        pass


class Manager(Employee):
    def calculate_bonus(self):
        return self.salary * 0.2


m = Manager("Pavan", 60000)
m.show_info()
print("Bonus:", m.calculate_bonus())

Manager.company_policy()
Employee.change_company("NextGenTech")
m.show_info()
