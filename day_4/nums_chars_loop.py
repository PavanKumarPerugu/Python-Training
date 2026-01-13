#nums with for
print("Output for Numbers printing Program using For")
for i in range(1, 6):
    print(i)

print("\nOutput for Numbers printing Program using For")
for i in range(1, 6):
    print(i, end=" ")
print()

#nums with while
print("\nOutput for Numbers printing Program using While")
def print_nums():
    i = 0
    while i<=10:
        print(i)
        i+=1
print_nums()

#chars with for
print("\nOutput for Character Program")
for ch in "Python":
    print(ch)


#break
print("\nOutput for Break Program")
for i in range(1, 6):
    if i == 3:
        break
    print(i)


#continue
print("\nOutput for Continue Program")
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
