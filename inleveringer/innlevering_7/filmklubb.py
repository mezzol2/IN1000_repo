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
        movie = Film(inp1,inp2)
        self._filmer.append(movie)
   