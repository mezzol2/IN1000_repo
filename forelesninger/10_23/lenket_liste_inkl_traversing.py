class Stasjon:
    def __init__(self, navn):
        self._navn = navn
        self._naboer = []
    
    def hent_navn(self):
        return self._navn

    def legg_til_nabo(self, nabo):
        self._naboer.append(nabo)
    
    def hent_neste(self):
        return self._neste
        
        
def bygg_trase():
    trikkestall = Stasjon("stallen")
    forrige = trikkestall
    for fil_linje in open("ruter.txt"):
        biter = fil_linje.strip()
        biter = biter.split()
        fra_stasjon_navn = biter[0]
        til_stasjon_navn = biter[1]
        fra_stasjon = Stasjon(fra_stasjon_navn)
        til_stasjon = Stasjon(til_stasjon_navn)
        fra_stasjon.legg_til_nabo(til_stasjon)
        til_stasjon.legg_til_nabo(fra_stasjon)
    return trikkestall


def hoved_program():
    denne = bygg_trase()
    maal = input("Hvor vil du reise til?: ")
    while denne.hent_navn() != maal:
        print(f"Reiser gjennom {denne.hent_navn()}")
        denne = denne.hent_neste()


hoved_program()