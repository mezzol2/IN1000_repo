from random import randint

class Stasjon:
    def __init__(self, navn):
        self._navn = navn
        self._naboer = []
    
    def hent_navn(self):
        return self._navn

    def legg_til_nabo(self, nabo):
        self._naboer.append(nabo)
    
    def hent_neste(self):
        return self._naboer[randint(0,len(self._naboer)-1)]
        
        
def bygg_trase():
    stasjonsbok = {}
    for fil_linje in open("ruter.txt"):
        biter = fil_linje.strip()
        biter = biter.split()
        fra_stasjon_navn = biter[0]
        til_stasjon_navn = biter[1]


        if not fra_stasjon_navn in stasjonsbok:
            stasjonsbok[fra_stasjon_navn] = Stasjon(fra_stasjon_navn)
        fra_stasjon = stasjonsbok[fra_stasjon_navn]
    
        if not til_stasjon_navn in stasjonsbok:
            stasjonsbok[til_stasjon_navn] = Stasjon(til_stasjon_navn)
        til_stasjon = stasjonsbok[til_stasjon_navn]
            

        til_stasjon = Stasjon(til_stasjon_navn)
        fra_stasjon.legg_til_nabo(til_stasjon)
        til_stasjon.legg_til_nabo(fra_stasjon)
    return stasjonsbok


def hoved_program():
    stasjonsbok = bygg_trase()
    fra = input("Hvor reiser du fra?: ")
    fra = stasjonsbok[fra]
    maal = input("Hvor vil du reise til?: ")
    denne = fra
    while denne.hent_navn() != maal:
        print(f"Reiser gjennom {denne.hent_navn()}")
        denne = denne.hent_neste()


hoved_program()