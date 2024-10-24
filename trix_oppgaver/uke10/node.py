class Node :
    def __init__(self, nytt) :
        self._innhold = nytt
        self._neste = None

    def nyEtterfolger (self, ny) :
        self._neste = ny

    def hentNeste (self) :
        return self._neste

    def hentInnhold(self):
        return self._innhold