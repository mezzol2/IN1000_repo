from random import randint
from celle import Celle

class Rutenett:
    def __init__(self, rader, kolonner):
        self._ant_rader = rader
        self._ant_kolonner = kolonner
        self._rutenett = self._lag_tomt_rutenett()

    def _lag_tomt_rutenett(self):
        #Make a matrix my adding rows to a list
        #The number of rows is equal to self._ant_rader
        matrix = []
        for i in range(self._ant_rader):
            ny_rad = self._lag_tom_rad()
            matrix.append(ny_rad)

        return matrix


    def _lag_tom_rad(self):
        #Make a row (list) with a number of None values equal the number of columns
        ny_rad = []
        for i in range(self._ant_kolonner):
            ny_rad.append(None)

        return ny_rad


    def fyll_med_tilfeldige_celler(self):
        #Iterate through each row
        for rad in range(self._ant_rader):
            #Iterate through each column
            for kolonn in range(self._ant_kolonner):
                self.lag_celle(rad,kolonn)

    def lag_celle(self, rad, kol):
        #Make a cell
        cell = Celle()
        #Randomly determine whether it is alive
        if randint(0,2) == 1:
            cell.sett_levende()
        #Put it in the rutenett
        self._rutenett[rad][kol] = cell


    def hent_celle(self, rad, kol):
        #If the cell exists, return it
        if (rad in range(self._ant_rader)) and (kol in range(self._ant_kolonner)):
            return self._rutenett[rad][kol]
        else:
            return None

    def tegn_rutenett(self):
        #'Clear' the terminal
        for i in range(10):
            print()
        
        #Iterate through each row
        for rad in range(self._ant_rader):
            #Create an empty sting to print the contents of the row
            rad_streng = ""
            #Iterate through each cell in the row and add its "drawing" to the string
            for kol in range(self._ant_kolonner):
                rad_streng += f"{self._rutenett[rad][kol].hent_status_tegn()} "
            #Print the row to the terminal
            print(rad_streng)


    def _sett_naboer(self, rad, kol):
        #Get our starting cell
        denne_cellen = self.hent_celle(rad, kol)

        #Get the cells in the row above and add them as neighbors
        over_rad = rad - 1
        for hver_kol in range(kol-1, kol+2):
            nabo = self.hent_celle(over_rad,hver_kol)
            #Add the neighbor if it exists
            if nabo is not None:    
                denne_cellen.legg_til_nabo(nabo)
        
        #Get the cells from each side and add them as neighbors
        nabo = self.hent_celle(rad, kol-1)
        #Add the neighbor if it exists
        if nabo is not None:
            denne_cellen.legg_til_nabo(nabo)
        #
        nabo = self.hent_celle(rad, kol+1)
        #Add the neighbor if it exists
        if nabo is not None:
            denne_cellen.legg_til_nabo(nabo)

        #Get the cells in the row below and add them as neighbors
        under_rad = rad + 1
        for hver_kol in range(kol-1, kol+2):
            nabo = self.hent_celle(under_rad,hver_kol)
            #Add the neighbor if it exists
            if nabo is not None:
                denne_cellen.legg_til_nabo(nabo)


    def koble_celler(self):
        #Set neighbors for each cell
        for rad in range(self._ant_rader):
            for kol in range(self._ant_kolonner):
                self._sett_naboer(rad, kol)

    def hent_alle_celler(self):
        #Make an empty list
        celle_liste = []
        
        #Iterate through the rutenett and add each cell to the list
        for rad in range(self._ant_rader):
            for kol in range(self._ant_kolonner):
                celle_liste.append(self.hent_celle(rad,kol))
        
        return celle_liste


    def antall_levende(self):
        #Get the list of cells
        celle_liste = self.hent_alle_celler()
        #Initialize a counting variable
        levende_celler = 0

        #Iterate through the list and count the living cells
        for cell in celle_liste:
            if cell.er_levende():
                levende_celler += 1
        
        return levende_celler