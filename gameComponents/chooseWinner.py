from gameComponents import gameVars

# define a win or lose function 
def winorlose(status):
	# print("inside winorlose function, the status is:", status)
	print("You", status, "! Would you like to battle again?")
	choice = input("Y / N? ")

	if choice == "N" or choice == "n":
		print("Well AI Rex will always be here\nwaiting...in the elevator for his opponent!\n Better luck next time!")
		exit()

	elif choice == "Y" or choice == "y":

		print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
		print("Time is ticking. You might not be able to see the fireworks!\n")

		gameVars.player_lives = 5
		gameVars.ai_lives = 5
		gameVars.player = False 

	else:
		print("Make a valid choice: Y or N")
		choice = input("Y / N: ")
