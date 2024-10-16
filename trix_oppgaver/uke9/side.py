class Side:
    def __init__(self, length, color):
        self.__length = length
        self._color = color
    
    def get_length(self):
        return self.__length
    
    def get_color(self):
        return self._color