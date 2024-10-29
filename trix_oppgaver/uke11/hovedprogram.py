from bil import Bil
from person import Person

def main():
    car1 = Bil("White", "Cadillac")
    car2 = Bil("Golden", "Lexus")
    car3 = Bil("Silver", "Ford")

    person1 = Person("John")
    person2 = Person("Sarah")

    person1.kjop_bil(car1)
    person1.kjop_bil(car2)

    person2.kjop_bil(car3)

    #person1.biler()
    #person2.biler()

    print()

    person2.lei_bil(person1)

    person1.biler()
    person2.biler()



main()