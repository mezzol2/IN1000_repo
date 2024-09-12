personer = {}

inp = input("Vil du legge til en ny person?\nSkriv 'j' om 'ja': ").lower()

while inp == 'j':
    name = input("Gi opp et navn: ").upper()
    age = input("Gi opp persons alder: ")
    personer[name] = age

    inp = input("Vul du legge til en annen person?\nSkriv 'j' om 'ja': ").lower()

letters = []
inp = 'j'

while inp == 'j':
    single_letter = '123'
    while len(single_letter) != 1:
        single_letter = input("Gi et bokstav: ").upper()
        if len(single_letter) != 1:
            print("Skrive ETT bokstav!")

    letters.append(single_letter)
    inp = input("Vil du sjekke et annet bokstav?\nSkriv 'j' om 'ja': ").lower()

name_list = list(personer.keys())

print(personer)

for name in name_list:
    for a in letters:
        if a in name[0]:
            print(f'{name}: {personer[name]}')