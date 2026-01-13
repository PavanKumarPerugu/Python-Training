num = int(input("Enter a number: "))
if -10 < num < 10:
    print("Single-digit number")
elif -100 < num < 100:
    print("Double-digit number")
else:
    print("Number has more than 2 digits")
