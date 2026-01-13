#1. * (right angled triangle) pattern using single loop
print("\n* (right angled triangle) pattern using single loop: \n")
for i in range(1, 5+1):
    print("* " * i)

#2. * (upsode-down right angled triangle) pattern using single loop
print("\n* (upsode-down right triangle) pattern using single loop: \n")
for i in range(5, 0, -1):
    print("* " * i)

#3. * (equilateral triangle) pattern using nested loops
print("\n* (equilateral triangle) pattern using nested loops: \n")
for i in range(1, 5+1):
    for j in range(1, 5+1):
      print("* " * i)