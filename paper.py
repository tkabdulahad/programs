#!/usr/bin/python3
import random
t=["Rock","Paper","Scissors"]
computer=t[randint(0,2)]
player=false
while player==false:
	player=input("Rock,Paper,scissors?")
	if player==computer:
		print("tie")
	elif player=="Rock":
		if computer=="paper":
			print("you lose",computer,"covers",player)
		else:
			print("you win",player,"smashes",computer)
	elif player=="paper":
			if computer=="scissor":
				print("you lose",computer,"cut", player)
			else:
				print("you win",player,"covers",computer)
	elif player=="scissors":
			if computer=="Rock":
				print("you lose",computer,"smashes",player)
			else:
				print("you win",player,"cut",computer)
	else:
				print("that's not a valid play.check your spelling")
				player=false
				
