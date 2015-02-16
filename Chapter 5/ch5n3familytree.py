# Who Is Your Dad?
# Uses the dictionary and menus.
SON_LIST = ["George Washington", "Winston Churchill", "Fidel Castro", "Joseph Stalin", "Juan Carlos"]
FAMILY_DATABASE = {"George Washington": "Augustine Washington", 
				   "Winston Churchill": "Randolph Churchill",
				   "Fidel Castro": "Angel Castro y Agriz",
				   "Joseph 'Jughashvili' Stalin": "Besarion Jughashvili",
				   "Juan Carlos": "Infante Juan"}
choice = None
while choice != "0":
	print(
	"""
	Who's Your Daddy
	
	0 - Exit
	1 - Find a father of a son
	2 - Add a father and a son
	3 - Change son's father
	4 - Delete father-son combination
	"""
	)
	choice = input("Select an option: ")
	if choice == "0":
		print("\nGoodbye.")
	elif choice == "1":
		print("\nSons you can find a father to: ", SON_LIST)
		son = input("Whose father you want to look up?: ")
		if son in FAMILY_DATABASE:
			father = FAMILY_DATABASE[son]
			print("\nThe father of", son, "is", father)
		else:
			print("\nSorry, but I can't find this person's father.")
	elif choice == "2":
		son = input("\nAdd someone's first and last name: ")
		if son not in FAMILY_DATABASE:
			father = input("\nNow add this person's father's first and last name: ")
			if father not in FAMILY_DATABASE:
				FAMILY_DATABASE[son] = father
				son = [son]
				SON_LIST += son
				print("\nSon and father added.")
			else:
				print("\nSorry, but this person is already a father to the other person.")
	elif choice == "3":
		son = input("\nWhose father's you want to change?: ")
		if son in FAMILY_DATABASE:
			father = input("\nAdd a new father: ")
			FAMILY_DATABASE[son] = father
			print("\nFather changed.")
		else:
			print("\nSorry, but this person is not on the list. Please add one.")
	elif choice == "4":
		print("\nSons you can remove from the list: ", SON_LIST)
		son = input("Who you want to remove from the list?: ")
		if son in FAMILY_DATABASE:
			del FAMILY_DATABASE[son]
			SON_LIST.remove(son);
			print("\nPerson removed from the list.")
		else:
			print("\nThis person is not on the list.")
	else:
		print("I'm sorry, but there is no such option.")
		
input("\n\nPress 'Enter' to exit.")
quit()
