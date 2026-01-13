import random

def guess_the_number():
  secret_number = random.randint(1, 20)
  attempts = 5

  while attempts > 0:
      guess = int(input("Guess a number (1–20): "))

      if guess == secret_number:
          print("You won!")
          break
      elif guess < secret_number:
          print("Too low!")
      else:
          print("Too high!")

      attempts -= 1
      print("Attempts left:", attempts)

  else:
      print("Game over! The number was", secret_number)
guess_the_number()