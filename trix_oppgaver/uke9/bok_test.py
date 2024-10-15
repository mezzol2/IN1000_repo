from bok import Bok
from bokhylle import Bokhylle

def program():

    book1 = Bok("Fellowship of the Ring", "JRR Tolkein", 1954)
    print(book1)
    assert book1._author == "JRR Tolkein"
    assert book1._publication_year == 1954

    book_list = [book1]

    shelf = Bokhylle(2, book_list)
    assert shelf.er_ledig_plass()

    book2 = Bok("Crescent City", "Sarah J Maas", 2024)
    book3 = Bok("I was a Teenage Slasher", "Stephen G Jones", 2024)

    assert shelf.legg_til_bok(book2)
    assert not shelf.legg_til_bok(book3)
    assert not shelf.er_ledig_plass()

    x = shelf.finn_bok("Crescent City", 2024)
    print(x)
    

program()