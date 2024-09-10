o_liste = []
o = "o"

for x in range(5):
    o_liste.append(o)

stjerneliste = []
star = "*"
for x in range(5):
    stjerneliste.append(star)

rutenett = [o_liste, stjerneliste]
rutenett.append(o_liste)

for e in rutenett:
    print(e)