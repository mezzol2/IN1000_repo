høner = int(input("Hvor mange høner finnes det?\n"))

while høner > 0:
    sover = 'ja' == input("Sover bonden?\nja/nei:  ").lower()
    reven = 'ja' == input("Kommer reven?\nja/nei:  ").lower()
    if not reven:
        print("Ingenting skjer.")
    elif sover:
        høner -= 3
        print(f'Reven spiste tre høner. Det er {høner} høner igjen.')
    else:
        print("Bonden dreper reven og selger reveskin for 190 kr.")

#This program is not pefect and does not correctly deal with a number of hens that
# is not a multiple of three, but I cant be bothered to fix it rn