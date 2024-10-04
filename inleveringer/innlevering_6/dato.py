#Define a class Dato
class Dato:
    #Define the instance variables
    def __init__(self, ny_dag:int, ny_maaned:int, nytt_aar:int) -> None:
        self._dag = ny_dag
        self._maaned = ny_maaned
        self._aar = nytt_aar
    
    #Define a method that returns the year
    def hent_aar(self):
        return self._aar
    
    #Define a method the returns in the date in day.month.year format
    def vis_dato(self):
        return f"{self._dag}.{self._maaned}.{self._aar}"
    
    #Define a method that checks the day number in the date
    def sjekk_dag(self, dag_nr:int):
        if self._dag == dag_nr:
            return True
        else:
            return False