from gjest import Gjest

class Rorbu:
    def __init__(self):
        self._gjester = []
    
    def leggTilGjest(self, gjest):
        for guest in self._gjester:
            guest.underhold(1)
        self._gjester.append(gjest)
    
    def fortellVits(self, funny_number:int):
        for guest in self._gjester:
            guest.underhold(funny_number)
    
    def hvorMorsomtHarViDet(self):
        funny_total = 0
        for guest in self._gjester:
            funny_total += guest.hentUnderholdningsverdi()
        
        funny_avg = funny_total / len(self._gjester)

        #print(f"{funny_total:.0f}")
        if funny_avg < 200:
            print("Kjedelig kveld")
        elif funny_avg < 400:
            print("Dette var jo litt gøy")
        elif funny_avg < 600:
            print("Dette var artig!")
        else:
            print("Dra på Lopphavet - bi dæ godtar no så gyt e!")
