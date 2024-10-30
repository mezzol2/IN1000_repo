class Person:
    def __init__(self, navn, adresse, postkode_og_by, land, tlfnummer, twitter_handle):
        self._navn = navn
        self._adresse = adresse
        self._poststed = postkode_og_by
        self._land = land
        self._tlfnummer = tlfnummer
        self._twitter = twitter_handle
        
    def skriv_ut_person(self):
        print(self._navn)
        print(self._adresse)
        print(self._poststed)
        print(self._land)
        print(self._tlfnummer)
        print(self._twitter)
    
    def endre_navn(self, navn:str):
        self._navn = navn

    def hent_navn(self):
        return self._navn
    
    def endre_adresse(self, adresse:str):
        self._adresse = adresse

    def hent_adresse(self):
        return self._adresse
    
    def endre_poststed(self, poststed:str):
        self._poststed = poststed
    
    def hent_poststed(self):
        return self._poststed
    
    def endre_land(self, land):
        self._land = land
    
    def hent_land(self):
        return self._land
    
    def endre_tlfnummer(self, tlfnummer):
        self._tlfnummer = tlfnummer
    
    def hent_tlfnummer(self):
        return self._tlfnummer
    
    def endre_twitter(self, twitter):
        self._twitter = twitter
    
    def hent_twitter(self):
        return self._twitter