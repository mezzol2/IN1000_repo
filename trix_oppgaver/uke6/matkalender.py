from random import randint
from random import sample

def les_inn_mat_fil(filnavn):
    file = open(filnavn, 'r')
    dict1 = {}

    for line in file:
        line = line.strip()
        line = line.split(',')
        dict1[line[0]] = line[1]
    
    file.close()

    return dict1

def velg_matretter(n, dict1):
    keys = list(dict1.keys())
    return sample(keys, n)

def skriv_matretter_til_fil(filename, food_options):
    file = open(filename, 'w')

    for item in food_options:
        file.write(item + '\n')


    file.close()



file = 'matratter.txt'
new_file = 'options.txt'
n = randint(0, 13)
foods = les_inn_mat_fil(file)

menu = velg_matretter(n, foods)

skriv_matretter_til_fil(new_file, menu)