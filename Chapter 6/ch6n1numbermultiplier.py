# Updated 'ask_number()' function.
# Adds the multiplier option.
multiplier = None
def ask_yes_no(question):
	"""Asks a question with answers 'yes' or 'no'."""
	response = None
	while response not in ("y", "n"):
		response = input(question).lower()
	return response

def ask_number(question, low, high, multiplier):
	"""Asks the player to input a number in a set range with the addition of multiplier."""
	response = None
	print("At the moment available numbers are from 1 to 100.")
	multchange = ask_yes_no("Current multiplier is 1. Do you wish to change it? (y/n): ")
	if multchange == "y":
		multiplier = int(input("\nPlease input a number for multiplier: "))		
		if multiplier == 0:
			print("\nYou can't put zero there!")
			multiplier = int(input("Please input a number for multiplier: "))
		else:
			print("\nMultiplier changed.")
			print("Multiplier is now", multiplier, "and that means you can only input a number multiplied by this one.")
	else:
		print("\nYou left the multiplier as it is.")
		multiplier = 1
	while response not in range(low, high, multiplier):
		response = int(input(question))
		if response not in range(low, high, multiplier):
			print("\nThe number is not in range of multiplier.")
		else:
			print("\nThis number is in range!")
	return response	
		
ask_number("Please input a number: ", 0, 100, multiplier)
input("\n\nPress 'Enter' to exit.")
quit()
