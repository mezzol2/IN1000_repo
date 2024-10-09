class NorskOrd:
    def __init__(self, ord:str) -> None:
        ord = ord.lower()
        self._ord = ord
    
    def sjekk_norske(self):
        bokstav = ['æ', 'ø', 'å']
        for letter in bokstav:
            if letter in self._ord:
                return True
        return False

    def skriv_ord(self):
        print(self._ord)

def hoved():
    word1 = NorskOrd('hello')
    word2 = NorskOrd("høst")

    assert word1.sjekk_norske() == False
    assert word2.sjekk_norske() == True

    words = ['høst', 'vinter', 'vår', 'sommer']
    for word in words:
        test_word = NorskOrd(word)
        if test_word.sjekk_norske():
            test_word.skriv_ord()
    

hoved()