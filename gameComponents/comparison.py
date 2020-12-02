from gameComponents import gameVars, chooseWinner, comparison 
from random import randint

def comparison(status):

	computer = gameVars.weapons[randint(0,2)]
	
	print("Auto chose: " + computer)

	
	if (computer == gameVars.player):
				print("tie")

	#always check for negative conditions
	elif (computer == "rock"):
		if (gameVars.player == "scissors"):
			print("you got hit by a rock...somehow!")
			gameVars.player_lives -= 1
		else:
			print("you win!")
			gameVars.ai_lives -= 1

	elif (computer == "paper"):
		if (gameVars.player == "rock"):
			print("AI Rex smacks you with a stack of files!")
			gameVars.player_lives -= 1
		else:
			print("you win")
			gameVars.ai_lives -= 1

	elif (computer == "scissors"):
		if (gameVars.player == "paper"):
			print("oof! AI Rex pinches your arm")
			gameVars.player_lives -= 1
		else:
			print("you win")
			gameVars.ai_lives -= 1