def inc_list(list1, num):
    list2 = []

    for number in list1:
        list2.append(number + num)
    
    return list2

def up_the_matrix(matrix):
    for i in range(len(matrix)):
        matrix[i]= inc_list(matrix[i],i + 1)
    
    return matrix

def print_lines(matrix):
    for row in matrix:
        print(row)


eksempel_matrise = [[0, 1, 2], [3, 2, 1], [1, 1, 0]]

print_lines(eksempel_matrise)

up_the_matrix(eksempel_matrise)
print()
print_lines(eksempel_matrise)