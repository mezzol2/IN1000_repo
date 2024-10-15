class Menneske:
    def __init__(self, navn:str, alder:int):
        self._navn = navn
        self._alder = alder
        self._er_fordeler = False
        self._barn = []
    
    def har_fodelsdag(self):
        self._alder += 1
        print(f"Happy Birthday!  {self._navn} is now {self._alder}.")
    
    def bytt_navn(self, nytt_navn:str):
        self._navn = nytt_navn
    
    def faar_barn(self, navn):
        child = Menneske(navn, 0)
        self._barn.append(child)
        self._er_fordeler = True
        print(f"{self._navn} has had a child named {navn}.")
    
    def hent_navn(self):
        return self._navn
    
    def hent_barn(self):
        return self._barn
    
    def hent_alder(self):
        return self._alder

def main():
    john = Menneske("John", 30)
    print(f"{john.hent_navn()} is {john._alder} years old.")
    john.bytt_navn("Jack")
    print(f"This person's new name is {john.hent_navn()}.")
    john.har_fodelsdag()
    john.faar_barn("Lil John")
    
    child_list = john._barn
    print(f"{john._navn}'s children:")
    for child in child_list:
        print(f"{child.hent_navn()}, {child.hent_alder()}")



main()