from person import Person

def les_inn_person(filnavn):
    fil_liste = []
    fil = open(filnavn,'r')
    
    for linje in fil:
        linje = linje.strip()
        fil_liste.append(linje)

    fil.close()

    human = Person(fil_liste[0],fil_liste[1], fil_liste[2], fil_liste[3], fil_liste[4], fil_liste[5])

    return human

def lagre_person(person):
    file = open("person.txt", 'w')

    file.write(person.hent_navn())
    file.write("\n")
    file.write(person.hent_adresse())
    file.write("\n")
    file.write(person.hent_poststed())
    file.write("\n")
    file.write(person.hent_land())
    file.write("\n")
    file.write(person.hent_tlfnummer())
    file.write("\n")
    file.write(person.hent_twitter())

    file.close()

def main():

    file = "guy.txt"
    human1 = les_inn_person(file)
    
    human1.skriv_ut_person()

    lagre_person(human1)

main()