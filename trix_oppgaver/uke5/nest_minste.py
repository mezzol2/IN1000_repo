def nest_minste(liste):

    minste = liste[0]
    
    for tall in liste:
        if tall < minste:
            minste = tall

    set1 = set(liste)
    set1.remove(minste)
    liste = list(set1)

    nest = liste[0]
    for tall in liste:
        if tall < nest:
            nest = tall

    return nest


liste = [1,1,2,2,3,4,5]
print(nest_minste(liste))