#This program uses a function to determine ticket price based upon the the user's age

#Define th function
def get_age():
    #Ask the user's age
    alder = int(input("Hvor gammel er du?\n"))
    
    #Define the variable billettpris
    billettpris = 0

    #Determine the ticket price based upone the user's age
    if alder <= 17:
        billettpris = 30
        type_billett = 'barnebillett'
    elif alder < 63:
        billettpris = 50
        type_billett = 'vanlig billett'
    else:
        billettpris = 35
        type_billett = 'pensjonistbillett'
    
    #Print the ticket price
    print(f'Du får en {type_billett} som koster {billettpris} kr.')

#Call the function
get_age()