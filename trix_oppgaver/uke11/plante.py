class Plante:
    def __init__(self, maks_grense_vann):
        self._vann_beholder = 0
        self._maks_gresne_vann = maks_grense_vann
        self._levende = True
    
    def vann_plante(self, vann_Cl):
        self._vann_beholder += vann_Cl
        if self._vann_beholder > self._maks_gresne_vann:
            self._levende = False
    
    def ny_dag(self):
        self._vann_beholder -= 20
        if self._vann_beholder < 0:
            self._levende = False

    def levende(self):
        return self._levende    
