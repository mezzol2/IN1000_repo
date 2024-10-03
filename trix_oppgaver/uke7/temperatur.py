class Temperatur:
    def __init__(self, temperatur:float, scale:str) -> None:
        if scale.lower() == 'celsius':
            self._c = temperatur
            self._f = (temperatur * 9/5) + 32
            self._k = temperatur + 273.15
        elif scale.lower() == 'fahrenheit':
            self._f = temperatur
            self._c = (temperatur - 32) * 5/9
            self._k = self._c + 273.15
        elif scale.lower() == 'kelvin':
            self._k = temperatur
            self._c = temperatur - 273.15
            self._f = (self._c * 9/5) + 32
        else:
            print('Invalid input.')
    
    def hent_celsius(self):
        return self._c
    
    def hent_fahrenheit(self):
        return self._f
    
    def hent_kelvin(self):
        return self._k