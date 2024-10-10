#Define the Film class
class Film:
    #Initialize the instance with title and year (år) parameters
    def __init__(self, tittel:str, år:int):
        self._tittel = tittel
        self._år = år
        #Skuespillere is initialized here as an empty dictionary so that we may add actors
        # to it later
        self._skuespillere = {}
    
    #Return the film's title
    def hent_tittel(self):
        return self._tittel

    #Add a new actor with their role to the skuespillere dictionary
    def ny_skuespiller(self, navn:str, rolle:str):
        #Check if the actor is already in the skuespillere dictionary
        if navn in self._skuespillere.keys():
            #If the actor is already in the dictionary, print en error message
            print(f"{navn} finnes alerede i systemet og kan ikke legges til igjen.")
        else:
            #If the actor is not in the dictionary, add them
            self._skuespillere[navn] = rolle
    
    #Define a method that returns a list of actors from a film
    #To do this, make a list of the keys of skuespillere
    def hent_skuespiller_navn(self):
        actor_list = list(self._skuespillere.keys())
        return actor_list
    
    #Define a method that prints the information about a film
    def skriv_ut_film(self):
        #Retrieve the list of actors
        actor_list = self.hent_skuespiller_navn()
        #Check if actor_list is empty
        if actor_list == []:
            #If no actors have been added, print just the film's name and it's year
            print(f"\n{self._tittel}({self._år}).")

        #Otherwise print title, year, actors, and their roles
        else:
            #Print the title and year
            print(f"\n{self._tittel}({self._år}). Medvirkende:")
            #Print the actor and their role using a loop
            for actor in actor_list:
                print(f"{actor} som {self._skuespillere[actor]}")