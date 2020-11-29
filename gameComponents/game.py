from random import randint
from gameComponents import gameVars, chooseWinner


while gameVars.player is False:
	print("++++++++++++++++// Welcome to the RPS Game //+++++++++++++++++++++")
	print("You are celebrating the new year in Rio de Janeiro. You want to  take part in the beach fireworks.\nJust before midnight, you decided to go to the hotel to pick up your camera...\nbut got stuck in the elevator.")
	print("YOU HAVE TO WIN A ROCK PAPER SCISSORS GAME AGAINST THE AI (REX, THE AI DOG) OF THE ELEVATOR TO LEAVE")
	print("   ,_____ ,\n  ,._ ,_. 7/\n j `-'     /\n |o_, o    |\n.`_y_`-,'   !\n|/   `, `._ `-,\n|_     |  _.'*|\n  >--,-'`-'*_*'``---.\n  | _* _*'-'         '")
	print("\nAI Rex Lives:", gameVars.ai_lives, "/", gameVars.total_lives, "hearts ")
	print("Player Lives:", gameVars.player_lives, "/", gameVars.total_lives, "hearts")
	print("XXXXXXXXXXXXXXXXXXXXXX PREPARE FOR BATTLE XXXXXXXXXXXXXXXXXXXXXXXX")
	print("-------------------------------------------------------------------")

	print("You can still back out of this battle by entering quit to exit")
	
	# player choice
	gameVars.player = input("OR you can scream LONG LIVE THE KING and choose your weapon\nby entering one of the provided weapons: rock, paper or scissors:\n")

	if player == "quit":
		print("You chose to quit. \nYou spent the night in the elevator and had a photoshoot with AI Rex...\nThanks for playing!")
		exit()

	computer = gameVars.weapons[randint(0,2)]
	
	print("-------------------------------------------------------------------")

	print("Player chose: " +  gameVars.player)
	print("Auto chose: " + computer)

		
	if gameVars.player_lives == 0:
	 	chooseWinner.winorlose("lost")

	if gameVars.ai_lives == 0:
	 	chooseWinner.winorlose("won")

	print("Player has:", gameVars.player_lives, "lives left")
	print("Auto has lives:", gameVars.ai_lives, "lives left")


	#make the while reloop by setting player back to False 
	gameVars.player = False 


