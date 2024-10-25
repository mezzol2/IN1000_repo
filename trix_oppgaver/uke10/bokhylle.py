from bok import Bok

class Bokhylle:
    def __init__(self, max_books:int, book_list:list):
        self._max_books = max_books
        self._book_list = book_list
    
    def er_ledig_plass(self):
        if len(self._book_list) < self._max_books:
            return True
        else:
            return False
    
    def legg_til_bok(self, book):
        if self.er_ledig_plass():
            self._book_list.append(book)
            return True
        else:
            return False
        
    def finn_bok(self,title:str, year:int):
        for book in self._book_list:
            if (book.hent_tittel() == title) and (book.hent_utgivelseaar() == year):
                return book

        return False
    
    def __str__(self):
        book_string = ""
        for book in self._book_list:
            book_string += f"{book.hent_tittel()}\n"
        return book_string