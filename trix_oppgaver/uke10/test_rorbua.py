from gjest import Gjest
from rorbu import Rorbu

def main():
    show = Rorbu()

    for i in range(100):
        guest = Gjest()
        show.leggTilGjest(guest)

    show.fortellVits(200)
    show.hvorMorsomtHarViDet()

    show.fortellVits(1000)
    show.hvorMorsomtHarViDet()






main()