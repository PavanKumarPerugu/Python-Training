n = int(input("Enter a Number: "))

for i in range(1, n+1):
    for j in range(1, n+1):
        print("*", end=" ")
    print()
print()

for i in range(1, n+1):
    for j in range(1, n+1):
        if i==j:
          print("* "*(i), end=" ")
    print()
print()

for i in range(n, 0, -1):
    for j in range(n, 0, -1):
        if i==j:
          print("* "*(i), end=" ")
    print()
print()

for i in range(n, 0, -1):
    print("  " * (n - i) + "* " * i)