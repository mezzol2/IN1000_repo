class Lyspære: #class anem
    #make a condtructor with a instance variable
    def __init__(self) -> None:
        self.på = False

    #return a boolean value: is the light on?
    def er_på(self):
        return self._på
    
    #Turn the light on
    def tenne(self):
        self._på = True
    
    #Turn the li9ght off
    def slukke(self):
        self._på = False