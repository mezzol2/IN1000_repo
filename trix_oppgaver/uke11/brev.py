class Brev:
    def __init__(self, avsender:str, mottaker:str):
        self._avsender = avsender
        self._mottaker = mottaker
        self._innhold = []
    
    def skriv_linje(self, tekst_streng:str):
        self._innhold.append(tekst_streng)
    
    def les_brev(self):
        print(f"Hei, {self._mottaker}!\n")
        
        for line in self._innhold:
            print(f"{line}")

        print(f"\nHilsen fra\n{self._avsender}")

    
