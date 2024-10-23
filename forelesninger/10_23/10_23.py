class Node :
    def __init__(self, nytt) :
        self._innhold = nytt
        self._neste = None

    def ny_etterfolger (self, ny) :
        self._neste = ny

    def hent_neste (self) :
        return self._neste
        
    def hent_innhold(self):
        return self._innhold


# Bygger opp lenkelisten
min_lenkeliste = Node("1")       # Lager forste element, innhold er bare lopende tall fra 1
denne = min_lenkeliste
for i in range(2,6):
    ny = Node(str(i))     # Øker innholdet med 1 for hvert element (bruker indeks i, starter m/ 2)
    denne.ny_etterfolger(ny)
    denne = denne.hent_neste()

# Løper gjennom (traverserer) lenkelisten, henter og printer innholdet i hvert objekt
denne = min_lenkeliste
while denne is not None:
    print(denne.hent_innhold()) 
    denne = denne.hent_neste()