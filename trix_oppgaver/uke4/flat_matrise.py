# eksempel_matrise = [[0, 1, 2], 
#                     [3, 2, 1], 
#                     [1, 1, 0]]

# ny_liste = []

# for liste in eksempel_matrise:
#     for digit in liste:
#         ny_liste.append(digit)

# print(ny_liste)


eksempel_3d_matrise = [
    [[0, 1, 2], [3, 2, 1]], 
    [[1, 1, 0], [4, 2, 3], [2, 1, 0]]
    ]

ny_liste2 = []

for matrix in eksempel_3d_matrise:
    for list2 in matrix:
        for digit2 in list2:
            ny_liste2.append(digit2)

print(ny_liste2)