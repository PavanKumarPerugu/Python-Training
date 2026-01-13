from operations.add import add
from operations.subtract import subtract
from operations.multiply import multiply
from operations.division import divide

print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = int(input("Choose operation: "))
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

if choice == 1:
    print(add(a, b))
elif choice == 2:
    print(subtract(a, b))
elif choice == 3:
    print(multiply(a, b))
elif choice == 4:
    print(divide(a, b))
else:
    print("Invalid choice")