# Anagrams Version 2
# Updated version of Anagrams
# Computer chooses a random word and chaotically rearranges the letters in it.
# The player's task is to restore the base word.
import random
# Let's create a list of words from which the computer will choose.
WORDS = ("python", "anagram", "simple", "complex", "answer", "toaster", "computer", "guitar", "fridge")
# Now let's choose a random word from the list with this:
word = random.choice(WORDS)
# Now we'll create a variable with which the player version of the word will be comparing:
correct = word
# Let's add in the point system:
score = 0
tries = 0
addscore = 100
# Starting the anagram:
jumble =""
while word:
  position = random.randrange(len(word))
  jumble += word[position]
  word = word[:position] + word[(position + 1):]
print(
"""
      Welcome to the 'Anagram' game!
    You need to rearrange letters to create an understandable word.
  (To exit, press 'Enter' without typing anything else.)
"""
)
print("This is the anagram: ", jumble)
tries += 1
guess = input("\nTry to guess the word in this anagram: ")
while guess != correct and guess != "":
  print("I'm afraid you are wrong.")
  addscore -= 10
  tries += 1
  guess = input("Try to guess the word in this anagram: ")
  if correct == 'python' and tries == 6:
    print("Hmm, seems like you are grasping. Perhaps it's a type of snake?")
  elif correct == 'anagram' and tries == 6:
    print("Hmm, seems like you are grasping. Maybe you need to look at the title?")
  elif correct == 'simple' and tries == 6:
    print("Hmm, seems like you are grasping. It's not that DIFFICULT in meaning, if you know what I mean.")
  elif correct == 'complex' and tries == 6:
    print("Hmm, seems like you are grasping. It's not that EASY in meaning, if you know what I mean.")
  elif correct == 'answer' and tries == 6:
    print("Hmm, seems like you are grasping. Well, guess what is obvious?")
  elif correct == 'toaster' and tries == 6:
    print("Hmm, seems like you are grasping. Okay, which device is designed for cooking bread?")
  elif correct == 'computer' and tries == 6:
    print("Hmm, seems like you are grasping. You are using it everyday. Even right now.")
  elif correct == 'guitar' and tries == 6:
    print("Hmm, seems like you are grasping. It's a musical instrument. Bards usually use it.")
  elif correct == 'fridge' and tries == 6:
    print("Hmm, seems like you are grasping. You usually put food in it.")
if guess == correct:
  print("Yes, that's right! You guessed it!\n")
  print("Tries: ", tries)
  score += addscore
  print("Score: ", score)
print("Thank you for playing.")
input("\n\nPress 'Enter' to exit.")
quit()
