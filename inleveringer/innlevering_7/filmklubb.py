#Import the Film class
from film import Film

#Define the Filmklubb class
class Filmklubb:
    #Define the instance variable with an empty list
    def __init__(self):
        self._filmer = []
    
    #Define a methods that read films from an external file
    def les_filmer_fra_fil(self, filnavn):
        #Open the file as read-only
        file = open(filnavn, 'r')

        #For each line/film in the file, format it and add it to the filmer list
        for line in file:
            #Format the line
            line = line.strip()
            line = line.split(";")
            #Create a Film instance
            movie = Film(line[0],int(line[1]))
            #Add the Film instance to the list
            self._filmer.append(movie)

        #Close the file
        file.close()
    
    #Define a method that prints information about all films
    def skriv_ut_alle_filmer(self):
        for movie in self._filmer:
            movie.skriv_ut_film()
    
    #Define a method that prompts the user for information about another film
    # and adds it to the list
    def registrer_film(self):
        print("Legg til en annen film.")
        inp1 = input("Tittel: ")
        print("År må ha 4 siffere og innholder bare tall.")
        inp2 = input("År: ")
        #Check if the year input is valid
        while (len(inp2) != 4) or not inp2.isnumeric():
            print("Året er ugyldig.")
            print("År må ha 4 siffere og innholder bare tall.")
            inp2 = input("År: ")
        #Make the year an integer
        inp2 = int(inp2)
        movie = Film(inp1,inp2)
        self._filmer.append(movie)
   
    #Define a method that searches for a film title or the start of the film title
    def finn_film_tittel(self, tittel:str):
        #Iterate through the list of films and check for a match
        for movie in self._filmer:
            if movie.sjekk_tittel(tittel):
                return movie
        #If there is no match, return None
        return None
    
    #Define a function that adds actors to films
    def legg_til_skuespiller(self, film):
        #Define a boolean variable that detemines whether the user wants to add
        # another actor
        add_actor = True

        #Define a loop to add more actors
        while add_actor:
            #Ask the user if they want to add an actor
            inp = input(f"Vil du legge til en skuespiller til {film.hent_tittel()}?\n[j/n]: ").lower()
            #Check if the user's input is valid
            while inp not in ['j','n']:
                print("Det svaret er ugyldig.")
                inp = input("Skriv 'j' for ja eller 'n' for nei:  ").lower()
            #End the loop if the user does not want to continue
            if inp == 'n':
                add_actor = False
            #Add an actor if the user wants to continue
            else:
                navn = input("Navn: ")
                rolle = input("Rolle: ")
                film.ny_skuespiller(navn,rolle)
    

    #Define a method that finds films from a given time period
    def finn_filmer_periode(self, år_1:int, år_2:int):
        #Create an empty list to contain the movies from the given period
        period_films = []
        #For each film in the list, check whether it is in the given year range
        for movie in self._filmer:
            if movie.sjekk_periode(år_1, år_2):
                #Add the film to the list if it is within the year range
                period_films.append(movie)
        
        return period_films
