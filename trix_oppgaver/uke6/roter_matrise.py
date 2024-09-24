def invert_matrix(matrix1):

    matrix2 = []

    for x in range(len(matrix1)):
        row = []
        for y in range(len(matrix1)):
            row.append(matrix1[y][x])
        matrix2.append(row)


    return matrix2


matriseEn = [
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9]
]

matrix2 = invert_matrix(matriseEn)

print(matrix2)