class Espresso_maskin:
    def __init__(self,makskapasitet:int):
        self.maks = makskapasitet
        self.mengde = makskapasitet

    def lag_espresso(self):
        if self.mengde >= 40:
            self.mengde -= 40
            print("An espresso was made.")
        else:
            print("There is not enough water to make an espresso.")
    
    def lag_lungo(self):
        if self.mengde >= 110:
            self.mengde -= 110
            print("A lungo was made.")
        else:
            print("There is not enough water to make a lungo.")
    
    def fyll_vann(self, ml:int):
        if (self.mengde + ml) <= self.maks:
            self.mengde += ml
            print(f"You added {ml} ml of water to the machine.")
            print(f"There is now {self.mengde} ml of water in the machine.")
        else:
            print("You cannot add that much water.")
    
    def hent_vann_mengde(self):
        return self.mengde