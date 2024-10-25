class Stasjon:
    def __init__(self, navn):
        self._navn = navn
        self._neste = None

    def hent_navn(self):
        return self._navn
    
    def sett_neste(self, neste):
        self._neste = neste

    def hent_neste(self):
        return self._neste

def bygg_trase():
    trikkestall = Stasjon("stallen")
    forrige = trikkestall
    for stasjons_navn in open("trase.txt"):
        denne = Stasjon(stasjons_navn.strip())
        forrige.sett_neste(denne)
        forrige = denne
    return trikkestall

def hovedprogram():
    denne = bygg_trase()
    maal = input("Hvor vil du reise til (alle reiser starter paa rikshospitalet): ")
    while denne.hent_navn() != maal:
        print("Reiser gjennom: ", denne.hent_navn())
        denne = denne.hent_neste()
        

hovedprogram()      

