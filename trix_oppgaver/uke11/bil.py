class Bil:
    def __init__(self, farge, merke):
        self._farge = farge
        self._merke = merke
        self._eier = None
    
    def sett_eier(self, eier):
        self._eier = eier
    
    def __str__(self):
        return f"{self._farge} {self._merke}"