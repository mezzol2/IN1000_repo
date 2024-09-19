def opprett_file(filnavn):
    from random import randint
    file = open(filnavn, 'a')
    for i in range(10):
        file.write(f'{str(randint(0,100))}\n')
    file.close()

def skriv_ut_foerste_linjer(filnavn, antall_linjer):
    file = open(filnavn, 'r')
    
    i = 0
    for line in file:
        if i < antall_linjer:
            print(line.strip())
            i += 1
    print('\n')

    file.close()

def skriv_ut_siste_linjer(filnavn, antall_linjer):
    file = open(filnavn, 'r')
    
    linjer = []
    for line in file:
        linjer.append(line.strip())

    last_lines = len(linjer)-antall_linjer

    for line in linjer[last_lines:]:
        print(line)

    file.close()

opprett_file('test.in')

skriv_ut_foerste_linjer('test.in', 5)

skriv_ut_siste_linjer('test.in', 5)