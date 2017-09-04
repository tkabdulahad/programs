#!/usr/bin/python3
import random 
count=0
r=0
while count<=200:
	roll=input("press r to roll the dice")
	if roll=="r":
		r=random.randint(1,6)
		count=count+r
		print("your random number is",r)
		print("you are on count",count)
		
