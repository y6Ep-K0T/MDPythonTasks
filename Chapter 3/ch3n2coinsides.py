# Coin Flip Game
# Test Work Number 2/4
# Uses the random selection algorhythm along with limited counter.
import random
heads = 0
tails = 0
drops = 0
print("\tWelcome to Coin Flips Calculator!")
print("\nThis program will count down 100 coin flips.")
print("Then it will determine how many times it flipped either heads or tails,")
print("and type in the amount.\n")
while drops < 100:
  coindrop = random.randint(0, 1)
  if coindrop == 0:
    heads += 1
    drops += 1
  elif coindrop == 1:
    tails += 1
    drops += 1
print("Coin was dropped 100 times. You got", heads, "heads and", tails, "tails.")
input("\n\nPress 'Enter' to exit.")
