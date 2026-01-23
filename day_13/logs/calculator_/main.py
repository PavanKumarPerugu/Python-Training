import logging
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from logs.calculator_.operations_.add_ import add
from logs.calculator_.operations_.subtract_ import subtract
from logs.calculator_.operations_.multiply_ import multiply
from logs.calculator_.operations_.division_ import divide

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(os.path.join(os.path.dirname(os.path.abspath(__file__)),"calculator.log"), mode="a"),  # logs to file
        logging.StreamHandler()  # logs to console
    ]
)

def calculator():
    logging.info("Calculator started.")
    
    while True:
        print("\n1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        try:
            choice = int(input("Choose operation: "))
        except ValueError:
            logging.warning("Invalid input: non-integer menu choice.")
            print("Please enter a valid integer choice.")
            continue
        
        if choice == 5:
            logging.info("Calculator exited by user.")
            print("Exiting the Calculator! Bye!!")
            break

        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
        except ValueError:
            logging.error("Invalid numeric input provided.")
            print("Please enter valid numeric values.")
            continue

        try:
            if choice == 1:
                result = add(a, b)
                logging.info(f"Performed addition: {a} + {b} = {result}")
                print("Sum is", result)
            elif choice == 2:
                result = subtract(a, b)
                logging.info(f"Performed subtraction: {a} - {b} = {result}")
                print("Difference is", result)
            elif choice == 3:
                result = multiply(a, b)
                logging.info(f"Performed multiplication: {a} * {b} = {result}")
                print("Product is", result)
            elif choice == 4:
                result = divide(a, b)
                logging.info(f"Performed division: {a} / {b} = {result}")
                print("Division is", result)
            else:
                logging.warning("Invalid menu choice entered.")
                print("Invalid choice! Enter a number from the listed options.")
        except Exception as e:
            logging.exception("Error occurred during operation:")
            print(f"Error: {e}")

if __name__ == '__main__':
    calculator()
