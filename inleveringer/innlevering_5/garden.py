#Does your garden suck?  This program endeavors to answer this question by asking
# the user what items they have in their garden, and giving them a rating


#Define a function that returns the external garden_reference file
def load_reference(filename):
    #Open the refence file
    file = open(filename, 'r')

    #Create a empty dictionary
    garden_dict = {}

    #Add items to the dictionay from the file
    for line in file:
        line = line.strip()
        line = line.split(',')
        garden_dict[line[0]] = line[1]
    
    #Close the file
    file.close()
    
    #Return the dictionary
    return garden_dict


#Define the initial prompt for the user
def initial_prompt():
    #Greet the user
    print("\nHello! Does your garden suck? Let's find out!\n")
    #Ask if they have a garden
    print("First, do you have a garden?")
    inp = input('Type "y" for yes, and "n" for no: ').lower()
    #If the user gives a reponse that is not y or n, ask them again
    while inp not in ['y', 'n']:
        print("\nThat answer is not recognized.")
        inp = input('Please type "y" for yes, and "n" for no: ').lower()
    #If the user does not have a garden, end the program
    if inp == 'n':
        exit("\nYou don't have a garden? Then why are you here? BYE.\n")
    #If the user has a garden, proceed
    print("\nGreat to hear that you have a garden.  Let's proceed.")

        
#Define a function that aks the user what is in their garden, and then gives them a rating
def calculate_rating(gard_dict):
    #Create a list of posible garden items from the dictionary
    garden_list = list(gard_dict.keys())
    #Create an empty list that the user can add garden items to
    user_list = []

    #For each item in the list, ask the user if that item in in their garden
    for item in garden_list:
        inp = input(f"\nDo you have {item} in your garden? [y/n]: ")
        #If the user gives an invalid response, ask them again
        while inp not in ['y', 'n']:
            print("\nThat answer is not recognized.")
            print(f"Do you have {item} in your garden?")
            inp = input('Type "y" for yes and "n" for no: ')
        #If the user answers yes, add the item to the user_list
        if inp == 'y':
            user_list.append(item)
    
    #If the user has no items in their garden, end the program
    if len(user_list) == 0:
        exit("\nYou have nothing in your garden?  Go buy a garden gnome or something.\n")


    #Calculate the users score based on the items in their garden
    #Start by initializing a score variable
    score = 0
    #Calculate a cumulative score
    for item in user_list:
        #Add the values from the garden dictionary
        score += float(gard_dict[item])
    #Convert score into an average
    score /= len(user_list)

    print(f"\nBased on your responses, your garden rates {score:.1f} out of 10.0.\n")
        

#Run the initial prompt for the user
initial_prompt()

#Load the garden_reference file
gard_dict = load_reference('garden_reference.txt')

#Ask the user what items they have, and give them a score
calculate_rating(gard_dict)