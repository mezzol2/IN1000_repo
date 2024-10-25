class Gjest:
    def __init__(self):
        self._underholdningsverdi = 0
    
    def hentUnderholdningsverdi(self):
        return self._underholdningsverdi
    
    def underhold(self, verdi:int):
        self._underholdningsverdi += verdi