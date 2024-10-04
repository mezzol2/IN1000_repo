#This program serves to test the Hund class

#Import the Hund class
from hund import Hund

#Define a procedure to run as the main program
def hovedprogram():
    #Create an instance of the Hund class
    dog1 = Hund(10, 20)
    
    #Test "hent" methods with assert statments
    assert dog1.hent_alder() == 10
    assert dog1.hent_vekt() == 20

    #Print information about the dog to the terminal
    print(f"\nHere we have a nice doggo named Zelda.")
    print("\nShe is a good doggo.")
    print(f"\nZelda is {dog1.hent_alder()} years old, and she weighs {dog1.hent_vekt()} kg.")

    #Have the dog jump two times
    for i in range(2):
        dog1.spring()
        print(f"\nZelda jumped!  She now weighs {dog1.hent_vekt()} kg.")
    
    #Check that metthet is now 8
    assert dog1._metthet == 8 

    #Have the dog eat twice
    for i in range(2):
        dog1.spis()
        print(f"\nZelda was hungry and ate some nice food.  She now weighs {dog1._vekt} kg.")

    #Check that metthet has returned to 10
    assert dog1._metthet == 10

    #Have a signoff for the program
    print("\nZelda gets some pets and wags her tail. Nice puppy.\n")

#Run the program
hovedprogram()