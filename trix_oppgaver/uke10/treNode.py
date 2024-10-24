class TreNode:
    def __init__(self, verdi:int):
        self._verdi = verdi
        self._venstre = None
        self._hoeyre = None
    
    def hentVerdi(self):
        return self._verdi

    def har_venstre_barn(self):
        if self._venstre is None:
            return False
        else:
            return True
    
    def har_hoeyre_barn(self):
        if self._hoeyre is None:
            return False
        else:
            return True
    
    def legg_til_barn(self, verdi:int):

        if verdi <= self.hentVerdi():
            if self._venstre is None:
                self._venstre = TreNode(verdi)
            else:
                self._venstre.legg_til_barn(verdi)
        else:
            if self._hoeyre is None:
                self._hoeyre = TreNode(verdi)
            else:
                self._hoeyre.legg_til_barn(verdi)

        
    
    def __str__(self):
        string =  f"node: {self._verdi}"
        if self.har_hoeyre_barn():
            string += f", right: {self._hoeyre._verdi}"
        if self.har_venstre_barn():
            string += f", left: {self._venstre._verdi}"
        
        return string
    
    def hent_sorterte_list(self):
        new_list = []

        if self.har_venstre_barn():
            new_list += self._venstre.hent_sorterte_list()

        new_list.append(self.hentVerdi())

        if self.har_hoeyre_barn():
            new_list += self._hoeyre.hent_sorterte_list()

        return new_list
    
    def skriv_ut_sortert(self):
        print(self.hent_sorterte_list())
    

    
    def søk_verdi(self, verdi):
        if verdi in self.hent_sorterte_list():
            return True
        else:
            return False
