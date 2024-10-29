class Student:
    def __init__(self, navn, brukernanvn, telefonnummer):
        self._navn = navn
        self._brukernavn = brukernanvn
        self._telefonnummer = telefonnummer

    def __str__(self):
        return f"Navn: {self._navn} \nBrukernavn: {self._brukernavn}\nTelefonnr: {self._telefonnummer}"
    
    def hent_navn(self):
        return self._navn