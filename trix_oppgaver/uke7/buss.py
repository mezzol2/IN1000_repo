class Buss:
    def __init__(self, max_capacity) -> None:
        self._max_cap = max_capacity
        self._passengers = 0
    
    def er_tom(self):
        if self._passengers == 0:
            return True
        else:
            return False
    
    def er_full(self):
        if self._passengers == self._max_cap:
            return True
        else:
            return False
    
    def plukk_opp(self):
        if Buss.er_full():
            print("The bus is full and cannot accept another passenger.")
        else:
            self._passengers += 1
            print(f"1 more passanger gets on the bus. There are now {self._passengers} passengers on board.")
    
    def slipp_av(self):
        if Buss.er_tom():
            print("The bus is empty.")
        else:
            self._passengers -= 1
            print(f"A passenger gets off the bus. There are {self._passengers} passengers left on the bus.")
    
    def hent_antall_passasjerer(self):
        return self._passengers