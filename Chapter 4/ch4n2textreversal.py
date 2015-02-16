# Text Reversal
# Reverses the user's text input.
text = input("Please enter any text. The computer will then reverse it: ")
revtext = ""
for i in range(len(text)-1, -1, -1):
  revtext+=text[i]

print("Here is your reversed text: ", revtext)
print("Have a nice day!")
input("\n\nPress 'Enter' to exit.")
quit()
