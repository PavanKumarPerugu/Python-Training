'''
1️⃣ Error Handling (try / except)

✅ Concept:

Error handling prevents your program from crashing when something unexpected happens.
'''

try:
    # code that might cause an error
    x = int(input("Enter a number: "))
    result = 10 / x
except ValueError:
    print("Please enter a valid integer!")
except ZeroDivisionError:
    print("Division by zero is not allowed!")
else:
    print("Result:", result)
finally:
    print("Execution completed.")



'''
2️⃣ File Exceptions

✅ Concept:

Errors often occur while working with files (missing file, permission denied, etc.).

'''

try:
    with open("data.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("Error: File not found.")
except PermissionError:
    print("Error: You don't have permission to read this file.")
