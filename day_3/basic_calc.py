def operations():
    print("\n--- *** Selctable Arithmetic Operations *** ---\n")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power")
    print("6. Exit")
  
def calc():
    operations()
    choice_of_operation = int(input("\nPlease select an operation from the enlisted operations above(1-6): "))
    match choice_of_operation:
        case 1:
            a = float(input("Please enter a number A: "))
            b = float(input("Please enter another number B: "))
            return f"Sum of A = {a} and B = {b} is {a+b}"
        case 2:
            a = float(input("Please enter a number A: "))
            b = float(input("Please enter another number B: "))
            return f"Difference of A = {a} and B = {b} is {a-b}"
        case 3:
            a = float(input("Please enter a number A: "))
            b = float(input("Please enter another number B: "))
            return f"Multiplication of A = {a} and B = {b} is {a*b}"
        case 4:
            a = float(input("Please enter a number A: "))
            b = float(input("Please enter another number B: "))
            return f"Division of A = {a} by B = {b} is {a/b}"
        case 5:
            a = float(input("Please enter a number A: "))
            b = float(input("Please enter a power number B: "))
            return f"A = {a} powered B = {b} is {a**b}"
        case 6:
            return f"\nThe Calculator is Exited. Good Bye!\n"
        case _:
            return f"\nYou have selected a wrong number! Please select from the enlisted operations\n"

while True:
    result = calc()
    if result != "\nThe Calculator is Exited. Good Bye!\n":
        print(result)
    else:
        print(result)
        break