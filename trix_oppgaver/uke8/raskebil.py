class RaskBil:
    def __init__(self, merke, bilnummer, navn, type_bil, maks_fart) -> None:
        self._merke = merke
        self._bilnummer = bilnummer
        self._navn = navn
        type_bil = type_bil.lower()
        self._type = type_bil
        self._maks = maks_fart
    
    def skrive_info(self):
        print(f"{self._navn} er en {self._merke} med bilnummer {self._bilnummer}.")
        print(f"Den bruker {self._type} og kan kjøre opptil {self._maks} km/t.")

def hoved():
    min_bil = RaskBil("Pontiac", "KNI667", "KITT", "Bensin", 150)
    min_bil.skrive_info()

hoved()