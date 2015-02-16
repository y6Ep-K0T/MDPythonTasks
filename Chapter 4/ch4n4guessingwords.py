# "The Guessing 2: Electric Boogaloo"
# Programm where you must guess the word, while given the number of letters in that word.
import random
WORDS = ("random", "book", "computer", "mouse", "cake", "paper", "shirt", "battery")
word = random.choice(WORDS)
print("Welcome to 'The Guessing 2: Electric Boogaloo'! Please don't mind the title.")
print("Here you must guess the letter based on the amount of letters given.")
print("You have 5 tries to guess a letter, then you must guess the word.")
print("Alright, here we go!\n")
print("Amount of letters: ", len(word))
tries = 0
print("Please guess a letter.\n")
while tries != 5:
  letter = input("It is ")
  if letter in word:
    print("Yes.")
    tries += 1
  else:
    print("No.")
    tries += 1
if tries == 5:
  guess = input("Now please guess the word: ")
if guess == word:
  print("Yes! You are right!")
  print("Thank you for playing.")
  input("\n\nPress 'Enter' to exit.")
  quit()
else:
  print("No. You are wrong.")
  input("\n\nPress 'Enter' to exit.")
  quit()
