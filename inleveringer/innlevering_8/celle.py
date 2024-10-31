class Celle:
    # Konstruktør
    def __init__(self):
        self._status = "doed"
        self._naboer = []
        self._ant_levende_naboer = 0
    
    def sett_doed(self):
        self._status = "doed"

    def sett_levende(self):
        self._status = "levende"

    #Check is the cell is living or dead
    def er_levende(self):
        if self._status == "levende":
            return True
        elif self._status == "doed":
            return False

    #If the cell is alive, return 'O', otherwise return '.'
    def hent_status_tegn(self):
        if self.er_levende():  #if True
            return "O"
        else:
            return "."

    def legg_til_nabo(self, nabo):
        self._naboer.append(nabo)

    def tell_levende_naboer(self):
        #Reset the ant_levende_naboer back to 0
        self._ant_levende_naboer = 0
        
        #Count the number of living neighbors
        for nabo in self._naboer:
            if nabo.er_levende():
                self._ant_levende_naboer += 1

    def oppdater_status(self):
        #Check if is the cell is alive:
        if self.er_levende():
            #Cell dies if it has any number of neighbors that is not 2 or 3
            if self._ant_levende_naboer not in [2,3]:
                self.sett_doed()
        
        #If the cell is dead, it becomes alive if it has exactly 3 neighbors
        else:
            if self._ant_levende_naboer == 3:
                self.sett_levende()