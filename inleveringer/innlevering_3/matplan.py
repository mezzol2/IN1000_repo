#This program contain information about hospital patients' meals
# and it can provide that information to the user

#Create the dictionary of patients
patients = {
    'Anduin Wrynn' : ['vanilla yoghurt', 'hot dog without sauce', 'boring salad'],
    'Alleria Windreunner' : ['chocolate', 'blood sausage', 'warm, black bread'],
    'Lady Prestor' : ['breakfast burrito', 'spicy soup', 'ghost peppers' ],
    'Thrall' : ['kebab', 'kebab', 'kebab'],
    'Illidan' : ['green yoghurt', 'steak', 'big salad']
}

#Define the fuction to get patients' meals
def get_meals():
    #Print patients' names
    patient_list = list(patients.keys())
    print(patient_list)
    #Whose meals would the user like to check
    name = input("Whose meal plan would you like to check?\n")

    #Print the meals if the patient exists
    if name in patients:
        print(patients[name])
    #Tell the user that name is not found
    else:
        print(f'{name} is not currently a patient.')
    
#Call the function
get_meals()


#Question 3
#3.a. set:  A set works best if someone needs just the usernames as there will be no repeated usernames.
#3.b. dictionary: A dictionary is needed to store usernames (keys) and corresponding studiepoeng (values).
#3.c. list: A list allows for repeated names which can happen with lottery winners.
#3.d. dictionary: A dictionary lets us store the name of the person (key), and the food they are allergic to (value).