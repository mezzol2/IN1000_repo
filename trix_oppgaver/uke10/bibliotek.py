from bok import Bok
from bokhylle import Bokhylle

class Bibliotek:
    def __init__(self, bokhylle_list:list = None):
        self._bokhylle_list = bokhylle_list
    
    def finnBokIBibliotek(self, title:str, pub_year:int):
        for book_shelf in self._bokhylle_list:
            returned_book = book_shelf.finn_bok(title, pub_year)
            if returned_book != False:
                return returned_book
        return False
    
    def utvidBibliotek(self):
        print("A new bookshelf is needed.")
        num = int(input("How many books spots will it have?  "))
        new_shelf = Bokhylle(num,[])
        self._bokhylle_list.append(new_shelf)
        return new_shelf


    def leggTilBokIBibliotek(self,book):
        ledigBokhylle = None
        
        #Check if there is a shelf with space
        for bok_hylle in self._bokhylle_list:
            if bok_hylle.er_ledig_plass():
                ledigBokhylle = bok_hylle
        
        #If not, make one
        if ledigBokhylle is None:
            ledigBokhylle = self.utvidBibliotek()

        ledigBokhylle.legg_til_bok(book)
                
