#This program shall let the user define a create a dictionary with email info,
# and let the user print that info when they want it


#Define a function that takes a name and returns a username
def lag_brukernavn(full_name):
    #Format the name to lowercase letters
    full_name = full_name.lower()
    #Split the name into list elements
    full_name = full_name.split()
    #Create the username from the list elements
    username = f'{full_name[0]}{full_name[1][0]}'
    #return the username
    return username


#Define a function that creates an email address
#The fuction shall use a username and suffix as inputs
def lag_epost(username, suffix):
    #Create the email address
    email = f'{username}@{suffix}'
    #Return the email address
    return email

#Define a fuctions that prints email address from dictionary information
#The given dictionary should have username and suffix information
def skriv_ut_eposter(user_dict):
    #Make a list of the users/keys in dictionary
    user_list = list(user_dict.keys())
    #Print an email for each user in the list
    for user in user_list:
        email = lag_epost(user, user_dict[user])
        print(email)

#Define a function that prompts the user
def prompt():
    print('\nType i to add a user.')
    print('Type p to print all known emails.')
    print('Type s to end the program.')
    inp = input('Your response: ').lower()
    #If the user gives an unknown response, prompt them again
    while inp not in ['i', 'p', 's']:
        print("That command is not recognized.  Please try again.")
        inp = input('Your response: ').lower()
    #Return the input
    return inp



#Create an empty dictionary to store user information
user_dict = {}

#Greet the user
print("\nHello! Here you can make and check email address for UiO user.")
#Promp the user for their initial choice
choice = prompt()
#Create a loop that runs as along as the user wants to continue (choice is not 's')
while choice != 's':
    #If the user wrote 'i', get info from the user to make and save an email
    if choice == 'i':
        #Prompt the user for information
        name = input("\nType the person's first and last name: ")
        suffix = input("Type their email suffix: ")
        #Create a username
        username = lag_brukernavn(name)
        #Add the information to the dictionary
        user_dict[username] = suffix
    #If the user wrote 'p', print the contents of the dictionary
    elif choice == 'p':
        print('\n')
        skriv_ut_eposter(user_dict)
    
    #Prompt the user for their next action
    choice = prompt()


#End the program
print("\nThank you! Have a good day!\n")