class Blueberry_plant:
    def __init__(self, height, num_berries:int) -> None:
        self._height = height
        self._num_berries = num_berries
        self._berry_weight = .03
    
    def get_plant_weight(self):
        return self._num_berries * self._berry_weight
    
    def water(self):
        self._height += 3
        self._num_berries += 5


def program():
    plant1 = Blueberry_plant(10, 2)
    assert plant1.get_plant_weight() == .06
    assert plant1._height == 10
    
    plant1.water()
    assert plant1.get_plant_weight() == .21
    assert plant1._height == 13



program()