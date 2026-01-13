'''
2️⃣ Create a Custom Exception Class (1 hr)

✅ Concept:

You can define your own exception types for clarity.

'''

class NegativeValueError(Exception):
    """Custom exception for negative values."""
    pass

def deposit(amount):
    if amount < 0:
        raise NegativeValueError("Amount cannot be negative!")
    print(f"Deposited ₹{amount} successfully.")

try:
    deposit(-500)
except NegativeValueError as e:
    print("Error:", e)
