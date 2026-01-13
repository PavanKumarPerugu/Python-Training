import requests

from_currency = input("Enter source currency (e.g., USD): ").upper()
to_currency = input("Enter target currency (e.g., EUR): ").upper()
amount = float(input("Enter amount to convert: "))

url = f"https://open.er-api.com/v6/latest/{from_currency}"

response = requests.get(url)
data = response.json()

if data["result"] != "success":
    print("Invalid currency code.")
    exit()

rate = data["rates"].get(to_currency)

if rate is None:
    print("Target currency not found.")
    exit()

converted_amount = amount * rate

print("\nCurrency Conversion")
print("-------------------")
print("From:", from_currency)
print("To:", to_currency)
print("Amount:", amount)
print("Converted Amount:", round(converted_amount, 2))
