def skriv_dna(filnavn):
    filnavn = open(filnavn, 'a')
    filnavn.write("O---o\n O-o \n  O  \n o-O \no---O")
    filnavn.close()

for i in range(3):
    skriv_dna('firstfile.txt')