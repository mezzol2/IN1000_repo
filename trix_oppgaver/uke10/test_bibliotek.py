from bok import Bok
from bokhylle import Bokhylle
from bibliotek import Bibliotek

def main():
    bok1 = Bok("Fellowship of the Ring", "JRR Tolkein", 1954)
    bok2 = Bok("Game of Thrones","George RR Martin", 1996)
    bok3 = Bok("Dune", "Frank Herbert", 1965)
    bok4 = Bok("Foundation", "Isaac Asimov", 1951)

    shelf1 = Bokhylle(2, [bok1, bok2])
    shelf2 = Bokhylle(2, [bok3, bok4])

    shelf_list = [shelf1, shelf2]

    my_library = Bibliotek(shelf_list)

    print(my_library.finnBokIBibliotek("Dune", 1965))
    assert not my_library.finnBokIBibliotek("Fake Book", 2000)




main()