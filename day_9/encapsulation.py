'''

1️⃣ Encapsulation — “ATM Machine” 🏧

- You can’t directly access bank’s internal data
- You interact via buttons & screen
- Balance is hidden

Concept
- Encapsulation = hiding internal data + controlled access

'''

class BankAccount:
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.__balance = balance  # private variable

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance")

    def get_balance(self):
        return self.__balance

acc = BankAccount("Alice", 1000)
acc.deposit(500)
print(acc.get_balance()) # acc.__balance cannot be accessed directly without defing by a method
