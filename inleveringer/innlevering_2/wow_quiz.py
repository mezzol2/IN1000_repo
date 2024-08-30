#Since the new World of Warcraft expansion has released, there many new
# and returning players to the game.  For these players, they may not
# be able to decide which class to play.  This program will try to help
# them in their decision making process.

#Greet the user and get their name
print("\nGreetings adventurer! Welcome to Azeroth!")
print("Before we can get started on your journey, I have a question.")
name = str(input("What is your name?\n"))


#Determine if a melee or ranged play style is better.
print(f"\n{name}!  That's a fine name indeed.  One that will be spoken of in future legends.")
print("Now, to determeine which class you should play, I will ask a series of questions.")
#Define a generic variable to determine responses
print(f"{name}, do you prefer to in the thick of the action of to fight at ranged?")
answer = input("Respond 1 for close-combat or 2 for ranged: ")