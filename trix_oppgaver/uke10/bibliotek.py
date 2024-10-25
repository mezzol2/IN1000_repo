from bok import Bok
from bokhylle import Bokhylle

class Bibliotek:
    def __init__(self, bokhylle_list:list = None):
        self._bokhylle_list = bokhylle_list
    
    def finnBokIBibliotek(self, title:str, pub_year:int):
        for book_shelf in self._bokhylle_list:
            if book_shelf.finn_bok(title, pub_year) != False:
                return book_shelf.finn_bok(title, pub_year)
        return False

