# Character Generator
# Uses the multimenu.
points = 30
STR = 5
END = 5
WIS = 5
AGI = 5
choice = None
choice2 = None
choice3 = None
while choice != "0":
	print(
	"""
	Character Generator.
	1 - Assign points.
	2 - Subtract points.
	3 - View character stats.
	0 - Exit.
	"""
	)
	choice = input("Select a option: ")
	print()
	if choice == "0":
		print("Goodbye.")
	elif choice == "1":
		while choice2 != "0":
			print("\nYou have", points, "to assign. Input a number of respective skill to assign a point to it.\n")
			print("1 - Strength (", STR, ")" )
			print("2 - Endurance (", END, ")" )
			print("3 - Wisdom (", WIS, ")" )
			print("4 - Agility (", AGI, ")" )
			print("0 - Confirm assigned points")
			choice2 = input("\nSelect an option: ")
			print()
			if choice2 == "1" and points == 0:
				print("You have no points to spend!")
			elif choice2 == "2" and points == 0:
				print("You have no points to spend!")
			elif choice2 == "3" and points == 0:
				print("You have no points to spend!")
			elif choice2 == "4" and points == 0:
				print("You have no points to spend!")
			elif choice2 == "0":
				print("Points assigned.")
			elif choice2 == "1":
				points -= 1
				STR += 1
			elif choice2 == "2":
				points -= 1
				END += 1
			elif choice2 == "3":
				points -= 1
				WIS += 1
			elif choice2 == "4":
				points -= 1
				AGI += 1
			else:
				print("There is no such option!")
	elif choice == "2":
		while choice3 != "0":
			print("\nYou have", points, ". Input a number of respective skill to subtract a point from it.\n")
			print("Points -", points)
			print("1 - Strength (", STR, ")" )
			print("2 - Endurance (", END, ")" )
			print("3 - Wisdom (", WIS, ")" )
			print("4 - Agility (", AGI, ")" )
			print("0 - Confirm subracted points")
			choice3 = input("\nSelect an option: ")
			print()
			if choice3 == "1" and STR == 0:
				print("You can't subtract ay points from that stat!")
			elif choice3 == "2" and END == 0:
				print("You can't subtract ay points from that stat!")
			elif choice3 == "3" and WIS == 0:
				print("You can't subtract ay points from that stat!")
			elif choice3 == "4" and AGI == 0:
				print("You can't subtract ay points from that stat!")
			elif choice3 == "0":
				print("Points subtracted.")
			elif choice3 == "1":
				points += 1
				STR -= 1
			elif choice3 == "2":
				points += 1
				END -= 1
			elif choice3 == "3":
				points += 1
				WIS -= 1
			elif choice3 == "4":
				points += 1
				AGI -= 1
			else:
				print("There is no such option!")
	elif choice == "3":
		print("\nHere are the stats of your character:\n")
		print("Strength -", STR)
		print("Endurance -", END)
		print("Wisdom -", WIS)
		print("Agility -", AGI)
	else:
		print("There is no such option!")

input("\n\nPress 'Enter' to exit.")
quit()
