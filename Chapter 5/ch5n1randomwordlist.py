# Random Word List
# Uses the random function and list.
import random
from random import shuffle
wordlist = ["General", "Temperature", "Python", "Monitor", "Oven", "Machine", "Jacket", "Mouse", "Television", "Table"]
shuffle(wordlist)
for word in wordlist:
	print(word)
input("\n\nPress 'Enter' to exit.")
quit()
