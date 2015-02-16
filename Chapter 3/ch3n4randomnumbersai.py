# Guess the Number in Reverse
# Tests the computer's algorithm AI
from random import randint
import time
def computer_guess(number):
  print("\nComputer is thinking...")  
  integermin = 1
  integermax = 100
  guess = randint(1, 100)
  tries = 1
  time.sleep(2)
  while guess != number:
    print("The computer takes a guess...", guess)
    print("Computer is thinking...")
    if guess > number:  
      integermax = guess - 1
      tries += 1
      time.sleep(2)
    elif guess < number:
      integermin   = guess + 1
      tries += 1
      time.sleep(2)
    guess = integermin+(integermax-integermin)//2

  print("The computer guessed the number! It's", number)
  print("It took", tries, "tries to guess!")
  input("\n\nPress 'Enter' to exit.")
  quit()

def main():
    print("\tWelcome to 'Guess the Number'!")
    print("\nThis time you are the one who sets the number!")
    print("And the computer will be the one trying to guess the number.")
    print("\nNow please think of a number from 1 to 100.")
    number = int(input("Enter a number: "))
    if number < 1 or number > 100:
        print("Must be in range [1, 100]")
    else:
        computer_guess(number)
        
main()
