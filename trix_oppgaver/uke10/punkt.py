from math import sqrt

class Punkt:
    def __init__(self, x:float, y:float, z:float):
        self._x = x
        self._y = y
        self._z = z

    def __str__(self):
        return f"{self._x},{self._y},{self._z}"
    
    def faaAvstand(self, other):
        avstand = sqrt((other._x - self._x)**2 + (other._y - self._y)**2 + (other._z - self._z)**2)
        return avstand
    
    def faaNaermestePunkt(self, point_list):
        closest_point = point_list[0]
        smallest_dist = self.faaAvstand(point_list[0])
        for point in point_list:
            if self.faaAvstand(point) < smallest_dist:
                smallest_dist = self.faaAvstand(point)
                closest_point = point
        return closest_point
            
