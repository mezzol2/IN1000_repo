def maks_besøk(besøker):
    maks = 0
    pasient = []

    for i in besøker:
        if len(i) > maks:
            maks = len(i)
            pasient = [besøker.index(i) + 1]
        elif len(i) == maks:
            pasient.append(besøker.index(i) + 1)

    return pasient

def færrest_besøk(besøker):
    færreste = 31
    pasient = []

    for i in besøker:
        if len(i) < færreste:
            færreste = len(i)
            pasient = [besøker.index(i) + 1]
        elif len(i) == færreste:
            pasient.append(besøker.index(i) + 1)

    return pasient    

def alle_besøk(besøker):
    total = 0
    for i in besøker:
        total += len(i)
    
    return total

def hvem_var_på_dato(besøker, dato):
    hvem = []
    for pasient in besøker:
        if dato in pasient:
            hvem.append(besøker.index(pasient) + 1)
    
    return hvem


besøker = [[4, 6], [3, 4, 5], [21, 22, 29]]
listeEn = [[31], [14, 15, 16, 17, 18]]
listeTo = [[1,2,3], [2, 3, 4], [28, 31], [14, 15, 16, 17, 18]]
listeTre = [[1,2,3], [2, 3, 4], [28, 31], [14, 15, 16, 17, 18], [1, 2, 4, 5], [9, 12, 16, 19], [21, 23, 25, 27, 28]]

print(maks_besøk(listeTo))
print(færrest_besøk(listeTo))
print(alle_besøk(listeTo))
print(hvem_var_på_dato(listeTo, 2))