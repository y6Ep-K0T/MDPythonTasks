# Guess the Number, v1.1
# Added the limit on tries.
import random
print("\tWelcome to the 'Guess the Number' game!")
print("\nI have chosen a natural number out from 1 to 100 range.")
print("Try to guess it with only 7 tries!\n")
# Starting values.
number = random.randint(1, 100)
guess = int(input("Your guess: "))
tries = 1
# 'Guessing' cycle.
while True:
  while guess != number:
    if guess > number:
      print("Lower...")
    else:
      print("Higher...")
    guess = int(input("Your guess: "))
    tries += 1
# Limit cycle.
    if tries >= 7 and guess != number:
      print("I'm sorry, but you failed to guess the number in 7 tries.")
      input("\n\nPress 'Enter' to exit.")
      quit()
    elif guess == number:
      print("You have successfully guessed the number! It really was", number)
      print("You have spent", tries, "tries while guessing the number!")
	  input("\n\nPress 'Enter' to exit.")
	  quit()
