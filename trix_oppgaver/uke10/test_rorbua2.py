from gjest import Gjest
from rorbu import Rorbu

def main():

    show1 = Rorbu()
    show2 = Rorbu()

    show1 = show2

    for i in range(50):
        show1.leggTilGjest(Gjest())
    
    for i in range(75):
        show2.leggTilGjest(Gjest())
    
    assert show1.hentAntallGjester() == 125
    assert show2.hentAntallGjester() == 125

    show1.hvorMorsomtHarViDet()

    show1.fortellVits(150)
    show1.hvorMorsomtHarViDet()

    show1.fortellVits(200)
    show1.hvorMorsomtHarViDet()

    show1.fortellVits(200)
    show1.hvorMorsomtHarViDet()


main()