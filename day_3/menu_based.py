def menu():
    print("\n==== MENU ====")
    print("1. Check Positive/Negative/Zero")
    print("2. Check Even or Odd")
    print("3. Find Greater of Two Numbers")
    print("4. Check Vowel or Consonant")
    print("5. Exit")

while True:
    menu()
    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        num = float(input("Enter a number: "))
        if num > 0:
            print("Positive")
        elif num < 0:
            print("Negative")
        else:
            print("Zero")

    elif choice == "2":
        num = int(input("Enter a number: "))
        if num % 2 == 0:
            print("Even")
        else:
            print("Odd")

    elif choice == "3":
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        if a > b:
            print("Greater number is", a)
        elif b > a:
            print("Greater number is", b)
        else:
            print("Both numbers are equal")

    elif choice == "4":
        char = input("Enter a character: ").lower()
        if char in 'aeiou':
            print("Vowel")
        else:
            print("Consonant")

    elif choice == "5":
        print("Exiting program. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
