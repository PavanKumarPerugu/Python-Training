#1. Wish function
def wish(n):
    return f"\nHello {n}, Elico wishes you a wonderful week ahead!"
result = wish(input("\nPlease let us know your name: "))
print(result)

#2. Positive, Negative, Even, Odd and Prime cheking function
def number_check():
    while True:
        print("\n*** This code checks for ***")
        print ("1. Positive Number")
        print ("2. Negative Number")
        print ("3. Even Number")
        print ("4. Odd Number")
        print ("5. Prime Number")

        n = int(input("\nPlease enter a number: "))
        if n == 0:
            print(f"\n{n} is zero!")
            
        if n > 0:
            for i in range(2, int(n**0.5)+1):
                if n%i == 0:
                    print(f"\n{n} is not a Prime Number!")
                    break
            else:
                print(f"\n{n} is Prime Number! and a Positive Number!")

        if n%2 == 0:
            if n > 0:
                print(f"\n{n} is an Even Number!, and a Positive Number!")
            else:
                print(f"\n{n} is an Even Number!, and a Negative Number!")
            
        if n%2 != 0:
            if n > 0:
                print(f"\n{n} is an Odd Number!, and a Positive Number!")
            else:
                print(f"\n{n} is an Odd Number!, and a Negative Number!")
        
        ip = input("\nPlease select y for another number or n for exit! : \n") 
        if ip != "y":
            break
number_check()

