class Student:
    def __init__(self, navn, poeng, antall_quiz) -> None:
        self._navn = navn
        self._poeng = poeng
        self._antall_quiz = antall_quiz
    
    def legg_til_quiz_score(self, nye_poeng):
        self._antall_quiz += 1
        self._poeng += nye_poeng
    
    def gjennomsnittlig_score(self):
        return self._poeng / self._antall_quiz
    
    def skriv_ut_info(self):
        print(f"Navnet er {self._navn}.")
        print(f"Poengtotal er {self._poeng}.")
        print(f"{self._navn} har deltatt i {self._antall_quiz} quizzer.")