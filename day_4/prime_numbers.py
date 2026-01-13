def prime_num(n):
    if n <= 1:
        return f"{n} is not a Prime Number!"
    elif n == 2:
        return f"{n} is a Prime Number!"
    else:
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return f"{n} is not a Prime Number!"
        return f"{n} is a Prime Number!"


result = prime_num(int(input("Enter a Number: ")))
print(result)