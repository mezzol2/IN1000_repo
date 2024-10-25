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

    for fil_linje in open("ruter_full.txt"):
        biter = fil_linje.strip().split()
        fra_navn = biter[0]
        til_navn = biter[1]
        
        if not fra_navn in stasjonsbok:
            stasjonsbok[fra_navn] = Stasjon(fra_navn)        
        fra_stasjon = stasjonsbok[fra_navn]

        if not til_navn in stasjonsbok:
            stasjonsbok[til_navn] = Stasjon(til_navn)
        til_stasjon = stasjonsbok[til_navn]

        fra_stasjon.legg_til_nabo(til_stasjon)
        til_stasjon.legg_til_nabo(fra_stasjon)

    return stasjonsbok

def hovedprogram():
    stasjonsbok = bygg_trase()
    fra = stasjonsbok[input("Hvor reise fra?: ")]
    maal = stasjonsbok[input("Hvor vil du reise til (alle reiser starter paa rikshospitalet): ")]
    denne = fra
    while denne != maal:
        print("Reiser gjennom: ", denne.hent_navn())
        denne = denne.hent_neste()
        

hovedprogram()      

