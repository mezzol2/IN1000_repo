def return_flagg():
    land = input('Skriv inn et land: ').lower()
    sjekk = input('Hvilken farge vil du sjekke: ').lower()

    if land in flaggOrdbok:
        farger = flaggOrdbok[land]
        print(farger)
        if sjekk in farger:
            print(f'{sjekk} er i {land}s flagg')
        else:
            print(f'{sjekk} er ikke i {land}s flagg')    




flaggOrdbok = {"norge" : ["rødt", "hvitt", "blått"], 
               "sverige" : ["blått", "gult"],
               "danmark" : ["rødt", "hvitt"],
               "finland" : ["hvitt", "blått"],
               "japan" : ["rødt", "hvitt"],
               "gabon" : ["grønt", "gult", "blått"],
               "storbritannia" : ["rødt", "blått", "hvitt"],
               "chile" : ["blått", "hvitt", "rødt"]}

print(flaggOrdbok)
print()

flaggOrdbok['usa'] = ["blått", "hvitt", "rødt"]

return_flagg()