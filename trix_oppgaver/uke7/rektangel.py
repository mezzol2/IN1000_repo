class Rektangel:
    def __init__(self, lengde:int, bredde:int):
        self._lengde = lengde
        self._bredde = bredde
    
    def oekLengde(self, oekning:int):
        self._lengde += oekning
    
    def oekBredde(self, oekning:int):
        self._bredde += oekning
    
    def areal(self):
        return self._lengde * self._bredde
    
    def omkrets(self):
        return self._lengde*2 + self._bredde*2
    
    def reduserLengde(self, reduksjon):
        if self._lengde - reduksjon > 0:
            self._lengde -= reduksjon
        else:
            print(f"Kan ikke redusere lengden med {reduksjon}.")