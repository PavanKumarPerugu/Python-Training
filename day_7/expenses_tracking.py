import csv
import os

# File path
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "expenses.csv")

# Create CSV file with header if it doesn't exist
if not os.path.exists(file_path):
    with open(file_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["date", "category", "amount"])


def add_expense():
    print("\nEnter expense details in the following format:")
    print("Date format     : YYYY-MM-DD   (example: 2026-01-08)")
    print("Category format : text         (example: food)")
    print("Amount format   : number       (example: 150.75)\n")

    date = input("Enter date      : ")
    category = input("Enter category  : ")
    amount = input("Enter amount    : ")

    with open(file_path, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([date, category, amount])

    print("Expense added successfully!\n")


def view_expenses():
    print("\n--- All Expenses ---")
    with open(file_path, "r") as f:
        reader = csv.reader(f)
        next(reader)  # skip header
        for row in reader:
            print(f"Date: {row[0]}, Category: {row[1]}, Amount: {row[2]}")
    print()


# Main loop
while True:
    print("Choose an option:")
    print("1. Add expense")
    print("2. View expenses")
    print("3. Exit")

    choice = input("Enter your choice (1/2/3): ")

    match choice:
        case "1":
            add_expense()
        case "2":
            view_expenses()
        case "3":
            print("Exiting Expense Tracker. Goodbye!")
            break
        case _:
            print("Invalid choice. Please enter 1, 2, or 3.\n")
