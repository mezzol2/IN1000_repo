#This program will test the functionality of the Person class.
# The program will do this by letting the user input a name, age, and 
# hobbies for an instance of a person.  Once the user is finished inputting
# hobbies, the program will print the given hobbies.

#Import the Person class
from person import Person

#Define the main program
def main_program():
    #Ask the user for information to make an instance of the Person class
    name = input("\nPlease input the person's name: ")
    age = int(input("Please input the person's age: "))
    #Create an instance of the Person class with the given information
    person1 = Person(name, age)

    #Define a boolean varaible that checks if the user want to add hobbies
    will_add_hobby = True

    #Define a loop that let's the user add hobbies for as long as they want
    while will_add_hobby:
        #Ask the user if they want to add a hobby
        inp = input(f"Do you want to add a hobby for {person1._name}?\nType 'y' for yes or 'n' for no: ").lower()
        #Check if the user's reponse is valid
        while inp not in ['y', 'n']:
            inp = input("That input is invalid. Type 'y' for yes or 'n' for no: ").lower()
        #Add another hobby if the user answers 'y'
        if inp == 'y':
            inp = input("Please type the hobby: ")
            person1._hobbies.append(inp)
        #End the loop if the user does not wish to continue
        elif inp == 'n':
            will_add_hobby = False
    
    #Print the hobbies for the person
    person1.print_all()



#Run the program
main_program()