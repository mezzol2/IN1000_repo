#This program will help the user make travelplans

#Initialize an empty list for places, and have the user add places to that list
steder = []
for i in range(5):
    print("\nPlease add a place you will visit.")
    inp = input(f"You have {5-i} places to add: ")
    steder.append(inp)

#Make a list for clothes and have the user add items to it
klesplagg = []
for i in range(5):
    print("\nPlease add clothing you want to bring.")
    inp = input(f"You have {5-i} articles of clothing to add: ")
    klesplagg.append(inp)

#Make a list for departure dates and have the user add dates to it
avreisedatoer = []
for i in range(5):
    print("\nPlease input a departure date.")
    inp = input(f"You have {5-i} dates to add: ")
    avreisedatoer.append(inp)

#Create reiseplan as a master list to contain the lists previously made
reiseplan = [steder, klesplagg, avreisedatoer]

#Print the contents of reiseplan on three seperate lines
for i in range(len(reiseplan)):
    print(reiseplan[i])

#Now the user will input two numbers in order create their travel plans
#First, ask which list the user wants to check
print("\nDo you want to check destinations, clothes, or departures dates?")
liste_indeks1 = int(input("Type 0, 1, or 2 to choose: "))

#Check whether the input is valid
while liste_indeks1 not in range(3):
    liste_indeks1 = int(input("\nThat value is invalid.  Please enter a value from 0 to 2: "))

#Ask the user which element they want to check
print(f"\nWhich part of that list do you want to check?")
liste_indeks2 = int(input("Type 0, 1, 2, 3, or 4: "))

#Check whether the input is valid
while liste_indeks2 not in range(5):
    liste_indeks2 = int(input("\nThat value is invalid.  Please enter a value from 0 to 4: "))

print(f"\nYou have selected {reiseplan[liste_indeks1][liste_indeks2]}.  Hope that helps!")