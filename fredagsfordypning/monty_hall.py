#Define the monty hall game within a function
def monty_hall():
    #import the random library
    import random

    #choose the door the car is behind at random
    bil = random.randint(0,2)

    #ask the user which door they will open
    #inp = int(input("Hvilken dør vil du åpne? Dør 0, 1, eller 2?\n"))
    #hardcode the user's input to always 0
    inp = 0

    #define of set of bil and inp
    chosen_set = {bil, inp}

    #the host will now open one of the other doors
    #if the contestant chose the door with car behind it, the host will open one of the other doors at random
    if bil == inp:
        if inp == 0:
            dør_åpnes = random.randint(1,2)
        elif inp == 2:
            dør_åpnes = random.randint(0,1)
        elif inp == 1:
            dør_åpnes = random.randint(0,1)
            if dør_åpnes == 1:
                dør_åpnes += 1
    #if the contestant chose a door with a goat behind it, the host will open the other door with a goat
    elif (inp == 0) or (inp == 1) or (inp ==2):
        if 2 not in chosen_set:
            dør_åpnes = 2
        elif 1 not in chosen_set:
            dør_åpnes = 1
        else:
            dør_åpnes = 0
    else:
        exit("Du har valgt en dør som ikke finnes.  Vennligst prøv på nytt.")

    #define a list of all doors and remove both the open door and chosen door to find the closed door
    list_doors = [0, 1, 2]
    list_doors.remove(inp)
    list_doors.remove(dør_åpnes)

    #ask the contestant if they will change doors
    #inp2 = input(f'Du har valgt dør {inp}. Verten åpner dør {dør_åpnes} å vise en geit. Vil du åpne dør {list_doors[0]}?\nja/nei? ').lower()   
    #hardcode for the user to always stay with the same door
    inp2 = "nei"

    def ending():
        if inp == bil:
            print(f"Verten åpner dør {inp}, og det finnes en bil bak.  Gratulerer! Du vinner!")
        else:
            print(f"Verten åpner dør {inp}, og det finnes en geit.  Bah!")

    #show the contestant their prize
    if inp2 == "ja":
        inp = list_doors[0]
        ending()
    elif inp2 == "nei":
        ending()
    else:
        print('Vett ikke hva du skrev.  Prøv på nytt.')

monty_hall()
