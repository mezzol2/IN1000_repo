class Person:
    def __init__(self, name:str):
        self._name = name
        self._spouse = None

    def status(self):
        if self._spouse:
            print(f"{self._name} is married to {self._spouse}.")
        else:
            print(f"{self._name} is single.")

    def giftSeg(self, person):
        self._spouse = person._name