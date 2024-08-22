#This program gives the user a menu and asks them what they
# want to eat.  Once the program has the user´s reponses,
# it will give the user feedback on their selections.

#Define food options as variables since the program will
# reference them more than once
hr1 = "Stor burger"
hr2 = "BBQ"
hr3 = "Vår fine salat"
tb1 = "Pommes frites"
tb2 = "Sennap"

#Print a blank line for readability in the terminal
print()

#Print the menu for the user to read
print("Velkommen til Austins Restaurant")
print()
print("Hovedretter")
print(hr1)
print(hr2)
print(hr3)
print()
print("Tilbehør")
print(tb1)
print(tb2)
print()

#Ask the user to choose 1 main dish and 1 side dish
print("Vennligst velg en hovedrett.")
valg_hr = input()
print("Vennligst velg ett tilbehør.")
valg_tb = input()

#Print a blank line for readability in the terminal
print()

#Check the user´s inputs and give a response
if (valg_hr == hr1 or hr2) and (valg_tb == tb2):
    print("Du spiser ikk nok grønnsaker!")
