#Since the new World of Warcraft expansion has released, there many new
# and returning players to the game.  For these players, they may not
# be able to decide which class to play.  This program will try to help
# them in their decision making process.

#Define a function that tells the user they entered an invalid value and end the program
def error_mess():
    print("\nIt seems you are an agent of the Burning Legion and have given a corrupted response.")
    exit("(Please try again with valid responses.)\n")


#Greet the user and get their name
print("\nGreetings adventurer! Welcome to Azeroth!")
print("Before we can get started on your journey, I have a question.")
name = str(input("What is your name?\n"))


#Determine if a melee or ranged play style is better.
print(f"\n{name}!  That's a fine name indeed.  One that will be spoken of in future legends.")
print("Now, to determeine which class you should play, I will ask a series of questions.")
print(f"\n{name}, do you prefer to in the (1) thick of the action, or to (2) fight at ranged?")
melee_ranged = int(input("Repond by entering one of the numbered responses (1 or 2): "))

#Support or damage
dps_support = int((input("\nDo want to (1) fight monsters directly or (2) aid your allies? ")))

#if the player likes support detemine if they should be a healer
if dps_support == 2:
    heal_supp = int((input("\nDo you want to (1) heal your allies' wounds or (2) boost thier power? ")))
    #if the user wants to be support, but not heal, they should be an Augmenation Evoker
    if heal_supp == 2:
        exit(f"\n{name}, you would be perfect as an Augmentation Evoker.  With your draconic powers, you can help your allies defeat enemmies.\n")
    
    #if the user wants to heal, figure determine what type of healer they should be
    elif heal_supp ==1:
        #If the user wants to be a melee healer, they coule be a Paladin or Monk
        if melee_ranged == 1:
            heal_melee = int(input(f'{name}, do you (1) pray to the light or (2) meditate in your free time? '))
            if heal_melee == 1:
                exit("\nYou would be a great Holy Paladin.\n")
            elif heal_melee == 2:
                exit("\nYour dedication to meditation would make you a great Monk.\n")
            else:
                error_mess()
        #if the user want to be a ranged healer, they can be a priest, shaman, druid, or evoker
        #ask the user for more information
        elif melee_ranged == 2:
            heal_ranged = int(input("Do you (1) praise the Light, (2) really like dragons, (3) a tree hugger, or (4) like totems?\n"))
            if heal_ranged ==1:
                exit("\nPraise the Light! You have chosen the path of a Priest.\n")
            elif heal_ranged == 2:
                exit("\nSee how scaley you are.  You shall be a Preservation Evoker.\n")
            elif heal_ranged == 3:
                exit("\nYou shall be one with nature.  Embrace the path of a Druid.\n")
            elif heal_ranged == 4:
                exit("\nßYour will heal the world with your totems.  You are a Shaman of the elements.\n")
            else:
                error_mess()
    else:
        error_mess()