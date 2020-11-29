from gameComponents import gameVars


def comparison (status):

	if (game.computer == game.player):
				print("tie")

	#always check for negative conditions
	elif (game.computer == "rock"):
		if (game.player == "scissors"):
			print("you got hit by a rock...somehow!")
			game.player_lives -= 1
		else:
			print("you win!")
			game.ai_lives -= 1

	elif (game.computer == "paper"):
		if (game.player == "rock"):
			print("AI Rex smacks you with a stack of files!")
			game.player_lives -= 1
		else:
			print("you win")
			game.ai_lives -= 1

	elif (game.computer == "scissors"):
		if (game.player == "paper"):
			print("oof! AI Rex pinches your arm")
			game.player_lives -= 1
		else:
			print("you win")
			game.ai_lives -= 1