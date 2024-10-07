class Frukt:
    def __init__(self, navn:str, vann_per_100g, spiselig) -> None:
        self._navn = navn
        self._vann_per_100g = vann_per_100g
        self._spiselig = spiselig
    
    def info(self):
        if self._vann_per_100g == None:
            vann_str = f"unknown water content"
        else:
            vann_str = f"{self._vann_per_100g} ml water per 100 grams"
        
        if self._spiselig:
            edible_str = "edible"
        else:
            edible_str = "inedible"
        
        return f"{self._navn}: {vann_str}, {edible_str}"
