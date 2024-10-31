from rutenett import Rutenett

class Verden:
    def __init__(self, rader, kolonner):
        self._rutenett = Rutenett(rader, kolonner)
        self._rutenett.fyll_med_tilfeldige_celler()
        self._rutenett.koble_celler()
        self._generasjonsnummer = 0

    def tegn(self):
        self._rutenett.tegn_rutenett()
        print(f"Generasjon: {self._generasjonsnummer}")
        print(f"Levende celler: {self._rutenett.antall_levende()}")


    def oppdatering(self):
        #Make a list of all cells
        celle_liste = self._rutenett.hent_alle_celler()

        #Have each cell count how many living neighobrs it has
        for celle in celle_liste:
            celle.tell_levende_naboer()
        
        #Have each cell update its status
        for celle in celle_liste:
            celle.oppdater_status()

        #Increase the generation number by 1
        self._generasjonsnummer += 1