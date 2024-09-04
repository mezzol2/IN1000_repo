liste_noestet = [[1,2,3],[4,5,6],[7,8,9]]
print(liste_noestet[0][0], liste_noestet[1][2], liste_noestet[2][1])

kolonn1 = 0
i = 0

while i < 3:
    kolonn1 += liste_noestet[i][0]
    i += 1

print(kolonn1)

rad1 = 0
i = 0

while i < 3:
    rad1 += liste_noestet[0][i]
    i += 1

print(rad1)
print(sum(liste_noestet[0]))
