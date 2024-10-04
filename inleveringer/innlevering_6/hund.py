#Define a class Hund
class Hund:
    #Define the instance variables of alder, vekt, and metthet
    def __init__(self, alder:int, vekt:int) -> None:
        self._alder = alder
        self._vekt = vekt
        self._metthet = 10

    #Define a method that returns alder
    def hent_alder(self):
        return self._alder
    
    #Define a method that returns vekt
    def hent_vekt(self):
        return self._vekt
    
    #Define a method that reduces metthet every time the dog jumps
    def spring(self):
        self._metthet -= 1
        if self._metthet < 5:
            self._vekt -= 1
    
    #Define a method that increases metthet every time the dog jumps
    def spis(self):
        self._metthet += 1
        if self._metthet > 7:
            self._vekt += 1