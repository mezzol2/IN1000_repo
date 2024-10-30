class Dag:
    def __init__(self, dato:str, nedbørtall:float):
        self._dato = dato
        self._nedbørtall = nedbørtall

    def get_date(self):
        return self._dato
    
    def get_nedbørtall(self):
        return self._nedbørtall
    
    def __str__(self):
        return f"{self._dato} : {self._nedbørtall} mm"