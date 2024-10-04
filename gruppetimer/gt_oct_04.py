class Hund:
    def __init__(self, navn, breed, alder, kjønn, vekt) -> None:
        self._navn = navn
        self._breed = breed
        self._alder = alder
        self._kjønn = kjønn
        self._vekt = vekt
    
    def endre_navn(self, nytt_nanv:str):
        self._navn = nytt_nanv
    
    def skriv_ut_hilsen(self):
        print(f"Voff, jeg heter {self._navn}, og jeg er {self._alder} år gammel.")
    
    def feire_bursdag(self):
        self._alder += 1
        print(f"{self._navn} er {self._alder}! Gratulerer med dagen! :D")

class Student:
    def __init__(self, linje:str, studiepeong:float, student_ID:int) -> None:
        self._linje = linje
        self._studiepoeng = studiepeong
        self._studentID = student_ID
    
    def skriv_ut(self):
        print("Linje: ",self._linje)
        print("Studiepoeng: ", self._studiepoeng)
        print("Student ID: ", self._studentID)
    
    def øk_poeng(self, poeng:float):
        self._studiepoeng += poeng


def run_program():
    dog = Hund("Sarah", "Chocolate Lab",4, "F", 20)
    assert dog._navn == "Sarah"
    dog.endre_navn("Charlotte")
    assert dog._navn == "Charlotte"
    dog.skriv_ut_hilsen()
    dog.feire_bursdag()

def student_program():
    austin = Student("PROSA", 5.45, 12345)
    austin.øk_poeng(1)
    austin.skriv_ut()

student_program()