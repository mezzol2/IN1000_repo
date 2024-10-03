#This program test the Motorsykkel class to see if it works as intended

#Import the class
from motorsykkel import Motorsykkel

#Define the main program as hovedprogram
def hovedprogram():
    #Create a variable bike1 with the Motorsykkel class
    bike1 = Motorsykkel('Harley Davidson', '12345')
    #Create a variable bike2 with the Motorsykkel class
    bike2 = Motorsykkel('Victory', '69420')
    #Create a variable bike3 with the Motorsykkel class
    bike3 = Motorsykkel('Yamaha', '20568')

    #Places the bikes in a list for convenient reference
    bike_list = [bike1, bike2, bike3]

    #Print the information on the bikes
    for bike in bike_list:
        bike.skriv_ut()
    
    #Increase the odomoter on bike3 by 10km, and then return the odometer
    bike3.kjor(10)
    print(f"\nThe odometer on the Yamaha is now {bike3.hent_kilometerstand()} km.\n")
        
    


#Run the program
hovedprogram()