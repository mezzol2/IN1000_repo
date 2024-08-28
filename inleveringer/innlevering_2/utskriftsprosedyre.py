#This program asks the user their name and where they live
#The program then greets the user and states where they live
#The program does this three times and utilizes a fuction to avoid redundant code

#Add a line for readability
print('')

#Define a fuction asking the user their name and location
def name_location ():
    name = input("What is your name?\n")
    place = input("Where are you from?\n")
    #Greet the user with their name and location
    print(f"\nHi {name} from {place}!\n")

#Run the function 3 times
name_location()
name_location()
name_location()