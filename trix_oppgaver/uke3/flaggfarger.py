def return_flagg():
    land = input('Skriv inn et land: ').lower()
    farger = flaggOrdbok[land]
    print(farger)

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