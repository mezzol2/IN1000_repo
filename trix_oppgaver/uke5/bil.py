def les_bil(filnavn):
    resultatet = {}

    for linje in open(filnavn):
        linje = linje.strip()
        kolonner = linje.split(':')
        resultatet[kolonner[0]] = kolonner[1]

    return resultatet

print(les_bil('bil.txt'))