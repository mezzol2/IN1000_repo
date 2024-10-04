#This program will serve to test the Dato class

#Import the Dato class
from dato import Dato

#Define a main program to test the class's functionality
def main_program():
    dato1 = Dato(15,1,2024)

    #Test the hent_aar method
    assert dato1.hent_aar() == 2024

    #Test the vis_dato method
    assert dato1.vis_dato() == "15.1.2024"

    #Test the sjekk_dag method
    assert dato1.sjekk_dag(15)

    #Print the year to the terminal
    print(f"\nAaret er {dato1.hent_aar()}.")

    #Save the date as a variable
    dato_streng = dato1.vis_dato()

    #Print "Loenningsdag!" if the day is the 15th, and "Nymåned, nye muligheter" if it is the 1st
    if dato1.sjekk_dag(1):
        print("Ny måned, nye muligheter.")
    elif dato1.sjekk_dag(15):
        print("Loenningsdag!")
    
    #Print the date to the terminal
    print(f"Datoen er {dato_streng}.\n")


#Run the program
main_program()