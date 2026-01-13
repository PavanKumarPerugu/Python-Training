'''
Inventory Management (1 hour)

Goal: Create a small OOP-based inventory system.

Requirements:

Add, remove, and list products

Each product has: name, price, and quantity

Update stock when items are sold

Example:

'''

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name} - ₹{self.price} ({self.quantity} in stock)"


class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)
        print(f"✅ Added {product.name}")

    def remove_product(self, name):
        for p in self.products:
            if p.name == name:
                self.products.remove(p)
                print(f"❌ Removed {name}")
                break
        else:
            print(f"⚠️ {name} not found in inventory")

    def list_products(self):
        if not self.products:
            print("📦 Inventory is empty.")
        else:
            print("\n📋 Current Inventory:")
            for p in self.products:
                print(" -", p)

    def sell_product(self, name, quantity):
        for p in self.products:
            if p.name == name:
                if p.quantity >= quantity:
                    p.quantity -= quantity
                    print(f"💰 Sold {quantity} of {name}")
                else:
                    print(f"⚠️ Not enough stock for {name}")
                break
        else:
            print(f"⚠️ {name} not found in inventory")


# --- Usage Example ---
inv = Inventory()

# Add products
inv.add_product(Product("Apple", 50, 100))
inv.add_product(Product("Banana", 10, 200))
inv.add_product(Product("Mango", 80, 50))

# List current products
inv.list_products()

# Sell some products
inv.sell_product("Apple", 20)
inv.sell_product("Banana", 50)

# List updated inventory
inv.list_products()

# Remove a product completely
inv.remove_product("Mango")

# Final list after removal
inv.list_products()
