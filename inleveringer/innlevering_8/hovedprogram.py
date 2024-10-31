from verden import Verden

#Checks if user input is an integer greater than 0
def check_if_integer(inp):
    #Make a list of the numbers 0 to 9 as string values
    int_list = []
    for i in range(10):
        int_list.append(str(i))

    #Check that only the numbers 0 to 9 are in the input
    for character in inp:
        if character not in int_list:
            return False
    
    #Check that the input is not less than 1
    inp = int(inp)
    if inp < 1:
        return False
    
    #Return True if all the tests were passed
    return True
    

def hovedprogram():
   
    #Greet the user and ask them how many rows and columns the game will have
    print("God dag, bruker.  Shall we play a game?")
    print("I dag skal vi spille The Game of Life.  Jeg bare trenger å vite hvor mange rader og kolonner spillet skal ha.")
    rader = input("Rader: ")
    kolonner = input("Kolonner: ")
    
    #Check the user's input
    while not check_if_integer(rader):
        print("Rad-input må være en heltall større enn 0.")
        rader = input("Rader: ")
    while not check_if_integer(kolonner):
        print("Kolonn-input må være en heltall større enn 0.")
        kolonner = input("Kolonner: ")


    #Convert input to integer values
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