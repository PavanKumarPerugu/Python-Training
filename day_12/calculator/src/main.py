from operations.add import add
from operations.subtract import subtract
from operations.multiply import multiply
from operations.division import divide

def calculator():
    
    while True:

        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit","\n")

        choice = int(input("Choose operation: "))
        
        if choice == 5:
            print("Exiting the Calculator! Bye!!","\n")
            break
        
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        if choice == 1:
            print("Sum is", add(a, b),"\n")
        elif choice == 2:
            print("Difference is", subtract(a, b),"\n")
        elif choice == 3:
            print("Product is", multiply(a, b),"\n")
        elif choice == 4:
            print("Division is", divide(a, b),"\n")
        else:
            print("Invalid choice! Enter the number from the enlisted choices!!","\n")

if __name__ == '__main__':
    calculator()