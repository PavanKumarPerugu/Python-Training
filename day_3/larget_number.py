a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

if a >= b and a >= c:
    print("Largest is", a)
elif b >= a and b >= c:
    print("Largest is", b)
else:
    print("Largest is", c)
