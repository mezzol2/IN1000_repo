class Vare:
    def __init__(self, beskrivelse:str) -> None:
        self._høyeste_bud = None
        self._beskrivelse = beskrivelse
    
    def by(self, bud):
        if (self._høyeste_bud == None) or (bud > self._høyeste_bud):
            self._høyeste_bud = bud
    
    def se_bud(self):
        if self._høyeste_bud is not None:
            return self._høyeste_bud
        else:
            print("ingen bud")

def program():
    compy = Vare("Computer")

    compy.se_bud()
    assert compy._høyeste_bud == None
    compy.by(20)
    assert compy.se_bud() == 20



program()