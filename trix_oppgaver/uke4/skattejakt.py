skattekart = [] # n lister med n elementer
n = 5 # størrelsen

# Lag n antall rader (lister)
for i in range(n):
    rad = []

    # Fyll listene med bokstaven "O"
    # n antall ruter per rad
    for e in range(n):
        rad.append("O")

    # Legg til hver rade ("O"-liste) i skattekart-listen vår
    skattekart.append(rad)

def print_skattekart(skattekart):
    for rad in skattekart:
        print(" ".join(rad))

treasure = []
inp = input("Do you want to play a 1 or 2 player game?\n")

if inp == "1":
    from random import randint
    treasure.append(randint(0,4))
    treasure.append(randint(0,4))
    skattekart[treasure[0]][treasure[1]] = "X"

elif inp == "2":
    loop = True

    while (len(treasure) != 2) or loop:
        treasure = []
        inp = input("Where do you want to hide the treasure?\nEnter two numbers from 0 to 4: ")
        inp = inp.split()


        for i in range(len(inp)):
            treasure.append(int(inp[i]))
            
        if len(treasure) != 2:
            print("TWO numbers are needed. Please try again.\n")
        else:
            for i in treasure:
                if i in range(5):
                    loop = False
                else:
                    print("At least one number is not between 0 and 4.  Please try again.\n")
                    break

    print(treasure)
    skattekart[treasure[0]][treasure[1]] = "X"
    print_skattekart(skattekart)

    for i in range(50):
        print()
else:
    exit("That was an invalid response.  Try again.")

print("You have 3 guesses to find the treasure.")
for i in range(3):
    guess = []
    inp = input(f"What is guess number {i+1}?\n").split()
    
    for g in range(len(inp)):
        guess.append(int(inp[g]))
    
    if guess == treasure:
        print(f"Congratulations! {guess} is correct!")
        break
    else:
        print(f'{guess} is not correct. You have {3-i-1} guesses remaining.')
        skattekart[guess[0]][guess[1]] = "#"

if guess != treasure:
    print("You did not find the treasure.  You are a shit pirate.")

print_skattekart(skattekart)