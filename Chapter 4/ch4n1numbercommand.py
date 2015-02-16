# Number Counter On-Command
# Counts when the user asks.
# Uses the 'range' function.
low = int(input("Greetings! Please input first number from which you start the count: "))
high = int(input("Now put in the second number. Remember: it must be higher than the previous number: "))
if high < low:
  print("You can't type in the number that's less than the previous one!")
  high = int(input("Put in the second number. Remember: it must be higher than the previous number: "))
mult = int(input("Now please put in the multiplier: "))
if mult == 0:
  print("You can't put zero there!")
  mult = int(input("Please put in the multiplier: "))
for i in range(low, high+1, mult):
  print(i, end=" ")
print("Here are your numbers. Have a nice day!")
input("\n\nPress 'Enter' to exit.")
quit()
