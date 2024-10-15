from person import Person

def main():
    man = Person("Brad Pitt")
    woman = Person("Angeline Jolie")

    man.status()

    man.giftSeg(woman)
    woman.giftSeg(man)

    man.status()

main()