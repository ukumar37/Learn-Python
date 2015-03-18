#Import the EXIT function
from sys import exit

#Define the function that asks user how much gold they want
def gold_room():
	print "this room is full of gold. How much do you take?"
	
	choice = raw_input("> ")
	how_much = int(choice)
	
	if how_much < 50: #if less than 50
		print "Nice, you're not greedy, you win!"
		exit(0)
	elif how_much >= 50: #if equal to or greater than 50
		dead("You greedy bastard!")
	else: #if blank or no input
		dead("Man, learn to type a number.")
	
	
	
	#if "0" in choice or "1" in choice:
	#	how_much = int(choice)
	#else:
	#	dead("Man, learn to type a number.")
		
	#if how_much < 50:
	#	print "Nice, you're not greedy, you win!"
	#	exit(0)
	#else:
	#	dead("You greedy bastard!")


#Define what happens in the room with the bear. This function is called if the user	picks left door
def bear_room():
	print "There is a bear here."
	print "The bear has a bunch of money."
	print "The fat bear is in front of another door."
	print "How are you going to move the bear?"
	bear_moved = False #Set the condition where the bear is not moving
	
	while True:
		choice = raw_input("> ") #Ask user how they will move the bear and offer 4 choices
		
		if choice == "take honey": #choice #1
			dead("The bear looks at you then slaps your face off.")
		elif choice == "taunt bear" and not bear_moved: #choice #2
			print "The bear has moved from the door. You can go through it now."
			
			bear_moved = True
		elif choice == "taunt bear" and bear_moved: #choice #3
			dead("The bear gets pissed off and chews your leg off.")
		elif choice == "open door" and bear_moved: #choice #4
			gold_room()
		else:
			print "I got no idea what that means."


#Define what happens in the room with the Cthulhu. This function is called if the user picks right door	
def cthulhu_room():
	print "Here you see the great evil Cthulhu."
	print "He, it, whatever stares at you and you go insane."
	print "Do you flee for your life or eat your head?"
	
	choice = raw_input("> ")
	
	if "flee" in choice:
		start()
	elif "head" in choice:
		dead("Well that was tasty.")
	else:
		cthulhu_room()


#This function is called if the user messes with the Bear/Cthuhlu by making a wrong choice
def dead(why):
	print why, "Good job!"
	exit(0)

#This is the very first function that starts the game where the user has to pick the left or right door	
def start():
	print "You are in a dark room."
	print "There is a door to your right and left."
	print "Which one do you take?"
	
	choice = raw_input("> ")
	
	if choice == "left":
		bear_room()
	elif choice == "right":
		cthulhu_room()
	else:
		dead("You stumble around the room until you starve.")

#Start the game
start()