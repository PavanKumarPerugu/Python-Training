#1. creating a tuple
print("\nCreating a tuple: ")
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

#2. reading from a tuple
print("\nReading from a tuple: ")
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])

#3. reading from a tuple
print("\nReading from a tuple: ")
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

#4. updating a tuple
print("\nUpdating a tuple: ")
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

#4. concatinating tuples
print("\nConcatinating tuples: ")
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y
print(thistuple)

#5. deleting teple elements
print("\nDeleting tuple elements: ")
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

#6. unpacking teple elements
print("\nUnpacking tuple elements: ")
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)

#7. unpacking teple elements
print("\nUnpacking tuple elements: ")
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)

#8. unpacking teple elements
print("\nUnpacking tuple elements: ")
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits
print(green)
print(tropic)
print(red)