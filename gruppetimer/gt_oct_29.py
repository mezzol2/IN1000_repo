#Exam oppgave 3 from 2022 exam

#3a
def karantene(vaksinert:bool, farge:str):
    if vaksinert:
        return 0
    elif farge == "grønn":
        return 3
    elif farge == "rød" or farge == "oransje":
        return 10

assert karantene(True, "grønn") == 0
assert karantene(False, "grønn") == 3
assert karantene(False, "rød") == 10


#3b
def tell_grader(fag,bsc,msc):
    my_list = [bsc, msc]

    if fag not in my_list:
        return 0
    elif len(set(my_list)) == 1:
        return 2
    else:
        return 1

it = "IT"
hist = "Historie"
mate_fag = "mate"
assert tell_grader(it, hist, mate_fag) == 0
assert tell_grader(it, it, hist) == 1
assert tell_grader(it, it, it) == 2


#3c
def fjern_vokaler(setning, vokal_liste):
    setning = setning.split()
    ny_setning = ""
    for word in setning:
        for vokal in vokal_liste:
            word = word.replace(vokal,"")
        ny_setning += f"{word} "
    
    return ny_setning



def fjern_vokaler2(setning, vokal_liste):
    ny_setning = setning
    for bokstav in setning:
        if bokstav in vokal_liste:
            ny_setning = ny_setning.replace(bokstav, "")
    
    return ny_setning



def fjern_vokaler3(setning, vokal_liste):
    ny_setning = ""
    for bokstav in setning:
        if bokstav not in vokal_liste:
            ny_setning += bokstav
    
    return ny_setning



setning = "This is a sentence."
vokal_liste = ['a','e','i','o','u']
print(setning)
print(fjern_vokaler(setning, vokal_liste))
print(fjern_vokaler2(setning, vokal_liste))
print(fjern_vokaler3(setning, vokal_liste))


#3d
def summer_rabatt(vareliste, førpris, nypris):
    total_rabatt = 0
    for vare in vareliste:
        total_rabatt += førpris[vare] - nypris[vare]

    return total_rabatt