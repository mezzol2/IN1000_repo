class Vare:
    def __init__(self, navn:str, pris:int, artikkelnummer:int, allgery_list:list, kategori:str):
        self._navn = navn
        self._pris = pris
        self._artikkelnummer = artikkelnummer
        self._allergy_list = allgery_list
        self._kategori = kategori
    
    def __eq__(self, annen_vare):

        if type(annen_vare) is not Vare:
            return False

        if self._artikkelnummer == annen_vare._artikkelnummer:
            return True
        else:
            return False
    
    def __str__(self):
        return f"Vare: {self._navn}, nmr: {self._artikkelnummer}, pris: {self._pris} kr\nallergener: {self._allergy_list}, kategori: {self._kategori}"
    
    def get_name(self):
        return self._navn




class Handlekurv:
    def __init__(self):
        self._vareliste = []
        self._totalpris = 0
    
    def legg_til_vare(self, ny_vare):
        self._vareliste.append(ny_vare)
        self._totalpris += ny_vare._pris
    
    def hent_ut_varer(self):
        for item in self._vareliste:
            print(f"{item.get_name()} ")




def main():
    names = ['eple', '1 kg kaffe', 'energidrikk', '12 egg']
    pris = [10, 50, 24, 40]
    IDnumbers = [11111,22222,33333,44444]
    allergens = [['frukt'], ['ingen'], ['frukt'], ['egg']]
    categories = ['frukt', 'kaffe', 'brus', 'egg']

    vare_liste = []

    for i in range(len(names)):
        ny_vare = Vare(names[i], pris[i], IDnumbers[i], allergens[i], categories[i])
        vare_liste.append(ny_vare)
    
    print()
    
    for vare in vare_liste:
        print(vare)
        print()
    
    assert not vare_liste[0] == vare_liste[1]
    assert vare_liste[0] == vare_liste[0]

    my_basket = Handlekurv()
    my_basket.legg_til_vare(vare_liste[2])
    my_basket.hent_ut_varer()


main()