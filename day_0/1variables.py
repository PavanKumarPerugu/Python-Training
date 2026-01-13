
#1. Variabls 
name = "Pavan" #string, statement
print(name)
x = 1; y = 2 #int
print (x,y) 
#other valid examples are name1, HEIGHT, my_name, _name etc., while the invalid ones are 123, test%, 1&same etc. (exceptions: reserverd words such as for, while, if, import etc.)



#2. Data Types
print(type(name)) #checking datatype
print(isinstance(name, str)) #checking the datatype of a perticular instance or an object
age = 4
print(isinstance(age, int))
area = 4.5
print(isinstance(area, int))
area = 4.5
print(isinstance(area, float))
area = float(4) #valid type conversion
print(isinstance(area, float)) 
area = float(4.5)
print(isinstance(area, int)) #datatype
floor = "1"
floor = float(floor) #valid type conversion from string to float
print(isinstance(floor, float)) #datatype
floor = "ground"
floor = int(floor) #invalid type conversion from string to int
print(isinstance(floor, int))
#other data types available are complex, bool, list, tuple, range, dict, set and object etc.



#3. Operators
x = 1; y = 2 #assignment operator
z = x + y #addition & assignment operations
print (z) 
#other operators are -, *, /, %, **, //, () etc.

