#This program gives the user a menu and asks them what they
# want to eat.  Once the program has the user´s reponses,
# it will give the user feedback on their selections.

#Define food options as variables since the program will
# reference them more than once
hr1 = "Stor burger"
hr2 = "BBQ"
hr3 = "Salat"
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
#if the input is not a valid main dish, end the program
if (valg_hr != hr1) and (valg_hr != hr2) and (valg_hr != hr3):
    print(f"{valg_hr} er ikke en gyldig hovedrett.")
    exit("Vennligst prøv på nytt.")

print("Vennligst velg ett tilbehør.")
valg_tb = input()
if valg_tb != tb1 and valg_tb != tb2:
    print(f"{valg_tb} er ikke et gyldig tilbehør.")
    exit("Vennligst prøv på nytt.")

#Print a blank line for readability in the terminal
print()

#Check the user´s inputs and give a response

#First, check if user chose no vegetables
if (valg_hr == hr1 or valg_hr == hr2) and (valg_tb == tb2):
    print("Du spiser ikke nok grønnsaker!")

#Check if user chose a vegetarian meal
elif valg_hr == hr3 and valg_tb == tb1:
    print("Du har valgt et vegetarmåltid.")

#Display what the user selected
else:
    print(f"Du har valgt {valg_hr} med {valg_tb}.")