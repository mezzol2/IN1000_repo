from side import Side

class Firkant:
    def __init__(self):
        self._top = None
        self._right = None
        self._bottom = None
        self._left = None
    
    def legg_til_side(self, side, location:str):
        location = location.lower()
        if location == 'l':
            self._left = side
        elif location == 'r':
            self._right = side
        elif location == 't':
            self._top = side
        elif location == 'b':
            self._bottom = side
    
    def fjern_side(self, location:str):
        location = location.lower()
        if location == 'l':
            self._left = None
        elif location == 'r':
            self._right = None
        elif location == 't':
            self._top = None
        elif location == 'b':
            self._bottom = None
    
    def er_fullstendig(self):
        if (self._left is not None) and (self._right is not None):
            if (self._top is not None) and (self._bottom is not None):
                return True
        return False
