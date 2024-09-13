#This program has the user make a sandwich and then rates the user's sandwich

#Define a dictionary with bread options
breads ={
    "white" : 5,
    "wheat": 2,
    "focaccia": 8,
    "sourdough": 4,
    "pretzel bun": 10,
    "brioche" : 9,
    "lettuce wrap": 1
}

#Define a dictionary with cheese options
cheeses  = {
    "cheddar": 6,
    "brie" : 8,
    "Jarlsberg": 2,
    "pepper jack": 4,
    "munster" : 10,
    "no cheese": 0
}

#Define a dictionary with protein options
proteins = {
    "bacon" : 10,
    "ham" : 5,
    "turkey" : 3,
    "halloumi" : 9,
    "tuna" : 1,
    "salami" : 7,
    "no protein" : 0
}

#Define a dictionary with topping options
toppings = {
    "mayonaise" : 2,
    "tomato" : 5,
    "olives" : 4,
    "mustard" : 7,
    "avacado" : 10,
    "no toppings": 0
}

#Define a function that creates a string from the dictionary keys
def make_string(dictionary):
    dict_list = list(dictionary.keys())
    dict_string = ''
    for i in range(len(dict_list)-1):
        dict_string += f"{i}. {dict_list[i]}, "
    dict_string = f"{dict_string}and {len(dict_list) - 1}. {dict_list[len(dict_list) - 1]}"
    print(dict_string)
    print(f"Please make your selection by typing a number from 0 to {len(dict_list)-1}.")
        

#Greet the user give them bread options
print("\nHello sandwich enjoyer!  Welcome to the sandwich rater!")
print("\nYour bread options are:")
make_string(breads)

#Create an empty string to store the user's choices, and ask the user for their bread choice
selections = []
inp = int(input())
bread_list = list(breads.keys())
selections.append(bread_list[inp])

#Tell the user which bread they have chosen, and prompt them to choose cheeses
print(f"You have chosen {selections[0]}.")
print("\nYour cheese options are:")
make_string(cheeses)
#Store the users choice
inp = int(input())
cheese_list = list(cheeses.keys())
selections.append(cheese_list[inp])
print(f"You have chosen {cheese_list[inp]}.")
#Ask the user if they want more cheeses
more = True
while more:
    inp = input("Do you want to add more cheese? [y/n]: ").lower()
    if inp == 'y':
        print("Cheese options:")
        make_string(cheeses)
        inp = int(input())
        selections.append(cheese_list[inp])
        print(f"You have chosen {cheese_list[inp]}.")
        #End the loop if the user does not want cheese, even though they are wrong
        if inp == len(cheese_list) - 1:
            more = False
    elif inp == 'n':
        more = False
    else:
        print("Your input was not understood.")

#Ask the user for protein choices.
print("\nYour protein options are:")
make_string(proteins)
#Store the users choice
inp = int(input())
protein_list = list(proteins.keys())
selections.append(protein_list[inp])
print(f"You have chosen {protein_list[inp]}.")
#Ask the user if they want more protein
more = True
while more:
    inp = input("Do you want to add another protein? [y/n]: ").lower()
    if inp == 'y':
        print("Protein options:")
        make_string(proteins)
        inp = int(input())
        selections.append(protein_list[inp])
        print(f"You have chosen {protein_list[inp]}.")
        #End the loop if the user chooses no protein
        if inp == len(protein_list) - 1:
            more = False
    elif inp == 'n':
        more = False
    else:
        print("Your input was not understood.")

#Ask the user for topping choices.
print("\nYour topping options are:")
make_string(toppings)
#Store the users choice
inp = int(input())
topping_list = list(toppings.keys())
selections.append(topping_list[inp])
print(f"You have chosen {topping_list[inp]}.")
#Ask the user if they want another topping
more = True
while more:
    inp = input("Do you want to add another topping? [y/n]: ").lower()
    if inp == 'y':
        print("Topping options:")
        make_string(toppings)
        inp = int(input())
        selections.append(topping_list[inp])
        print(f"You have chosen {topping_list[inp]}.")
        if inp == len(cheese_list) - 1:
            more = False
    elif inp == 'n':
        more = False
    else:
        print("Your input was not understood.")


#calculate the user's sandwich score
score = 0
for i in range(len(selections)):
    if selections[i] in breads:
        score += breads[selections[i]]
    if selections[i] in cheeses:
        score += cheeses[selections[i]]
    if selections[i] in proteins:
        score += proteins[selections[i]]
    if selections[i] in toppings:
        score += toppings[selections[i]]

score /= len(selections)

#Return the user's selections as a string
string = ""
for i in range(len(selections)-1):
    string += f" {selections[i]},"
print(f"You have built a sandwich with{string} and {selections[len(selections)-1]}.")

#Tell the user their score
print(f'\nYour sandwich score is {score:.2f}.\n')