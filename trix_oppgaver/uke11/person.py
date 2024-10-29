from bil import Bil

class Person:
    def __init__(self, navn):
        self._navn = navn
        self._mine_biler = []
        self._laante_biler = []
    
    def biler(self):
        print(f"\n{self._navn}")

        print(f"\nOwned Cars:")
        for bil in self._mine_biler:
            print(bil)
        
        print(f"\nBorrowed Cars:")
        for bil in self._laante_biler:
            print(bil)
    
    def hent_mine_biler(self):
        return self._mine_biler
    
    def kjop_bil(self, bil):
        self._mine_biler.append(bil)
        bil.sett_eier(self)
    
    def lei_ut_bil(self):
        bil = self._mine_biler[-1]
        self._mine_biler.pop()

        return bil


    def lei_bil(self, utleier):
        if self._mine_biler == []:
            print(f"{utleier} har ingen biler å leie ut.")
        else:
            bil = utleier.lei_ut_bil()
            self._laante_biler.append(bil)