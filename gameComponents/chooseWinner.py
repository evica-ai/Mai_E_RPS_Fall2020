from gameComponents import gameVars

# define a win or lose function 
def winorlose(status):
	# print("inside winorlose function, the status is:", status)
	print("You", winorlose.status, "! Would you like to battle again?")
	choice = input("Y / N? ")

	if choice == "N" or choice == "n":
		print("You chose to quit! Better luck next time!")
		exit()

	elif choice == "Y" or choice == "y":

		gameVars.player_lives = 5
		gameVars.ai_lives = 5
		gameVars.player = False 

	else:
		print("Make a valid choice: Y or N")
		choice = input("Y / N: ")
