class Gruppe:
    def __init__(self,krav:list):
        self._krav = krav
        self._personer = []
    
    def legg_til_personer(self,personer:list):
        self._personer += personer
        
    def hent_personer(self):
        return self._personer
    
    def hent_krav(self):
        return self._krav


class Rom:
    def __init__(self, nummer:int, senger:int, fasiliteter:list):
        self._nummer = nummer
        self._senger = senger
        self._fasiliteter = fasiliteter
        self._gruppe = None
    
    def reserver(self, gruppe:list):
        self._gruppe = gruppe
    
    def hent_ant_senger(self):
        return self._senger
    
    def passer(self, kraver):
        if self._gruppe is not None:
            return False

        for krav in kraver:
            if krav not in self._fasiliteter:
                return False
        
        return True
    
    def __str__(self):
        return f"Rom: {self._nummer}\nSenger: {self._senger}\nFasiliteter: {self._fasiliteter}"


class Hotell:
    def __init__(self, hotellnavn:str):
        self._hotellnavn = hotellnavn
        self._rommer = {}
        filnavn = f"{hotellnavn}.txt"
        fil = open(filnavn, 'r')

        for linje in fil:
           linje = linje.strip()
           linje = linje.split()
           facilities = []
           for facility in linje[2:]:
                facilities.append(facility)
           rom = Rom(linje[0], int(linje[1]), facilities)
           self._rommer[linje[0]] = rom

        fil.close()
        