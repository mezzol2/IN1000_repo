from verden import Verden

def hovedprogram():
   
    #Greet the user and ask them how many rows and columns the game will have
    print("God dag, bruker.  Shall we play a game?")
    print("I dag skal vi spille The Game of Life.  Jeg bare trenger å vite hvor mange rader og kolonner spillet skal ha.")
    rader = input("Rader: ")
    kolonner = input("Kolonner: ")
    
    #Come back to filter input
    rader = int(rader)
    kolonner = int(kolonner)

    #Create the board, and draw the first generation
    brett = Verden(rader,kolonner)
    brett.tegn()

    #Ask the user if they will continue
    gå_videre = True
    while gå_videre:
        print("\nVil du se den neste generasjonen? ")
        inp = input("Trykk Enter å gå videre eller 'q' å bli ferdig: ").lower()
        #Filter the user's input
        while inp not in ['q',""]:
            print("Det svaret er ukjent.")
            inp = input("Trykk Enter å gå videre eller 'q' å bli ferdig: ").lower()
        
        #If the user is finished, end the game
        if inp == 'q':
            gå_videre = False
        
        #If the user will contine, update the board, and draw it again
        if inp == "":
            brett.oppdatering()
            brett.tegn()



# starte hovedprogrammet
hovedprogram()