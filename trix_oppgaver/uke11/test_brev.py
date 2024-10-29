from brev import Brev

def main():

    letter = Brev("Jeg", "Du")

    letter.skriv_linje("Hvordan har du det?")
    letter.skriv_linje("Jeg har det bare bra!")

    letter.les_brev()



main()