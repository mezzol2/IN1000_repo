class Kube:
    def __init__(self, lengde, bredde, dybde):
        self._lengde = lengde
        self._bredde = bredde
        self._dybde = dybde
    
    def __repr__(self):
        return f"\nlength: {self._lengde}\nwidth: {self._bredde}\ndepth: {self._dybde}"
    
    def __gt__(self,other):
        vol = self._lengde*self._bredde*self._dybde
        other_vol = other._lengde*other._bredde*other._dybde
        if vol > other_vol:
            return True
        else:
            return False
