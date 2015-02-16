# 'Surprise!' Cake Simulator
# Uses the 'random event' code.
import random
print("\tWelcome to the ''Surprise!' Cake' simulator!")
print("\nYou have been served a cake, which contains a surprise. You were told that there were 5 surprises in total.")
print("So, you put a knife on the center of the cake to take out a slice, and then...\n")
surprise = random.randint(1, 5)
if surprise == 1:
  print("...your knife hits something metallic. It is the miniature bowling ball!")
elif surprise == 2:
  print("...out from the cake pops a jack-in-the-box! That was a nice jumpscare there.")
elif surprise == 3:
  print("...something comes out from the center! It seems to be a tiny chest with something inside.")
elif surprise == 4:
  print("...the cake explodes. Well, someone seems to be on the line for cleanup.")
elif surprise == 5:
  print("...a clawed paw grabs the knife, and an angry faerie dragon comes out and casts something on you, then flies off.")
  print("You now have a beard and huge eyebrows! Don't worry, it'll wear off in a couple of hours.")
print("\nYou eat the cake along with the others and go to sleep.")
print("Perhaps next time they serve a cake, you'll get another surprise?")
input("\n\nPress 'Enter' to exit.")
