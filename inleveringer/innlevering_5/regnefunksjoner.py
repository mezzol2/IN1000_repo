#This program defines several calculation functions, and them calls them with
# a final procedure at the end

#Define an addition function
def addisjon(a,b):
    a += b
    return a

#Test the addisjon function
print(addisjon(29,34))



#Define a subtraction function
def subtraksjon(a,b):
    a -= b
    return a

#Test the subtraksjon function
assert subtraksjon(100, 20) == 80
assert subtraksjon(100,-20) == 120
assert subtraksjon(-100, -20) == -80



#Define a division function
def divisjon(a,b):
    a /= b
    return a

#Test the divisjon function
assert divisjon(100, 20) == 5
assert divisjon(100,-20) == -5
assert divisjon(-100, -20) == 5



#Define a function that converts inches (tommer) to centimeters
def tommer_til_cm(antall_tommer):
    #Check that antall_tommer is larger than 0
    assert antall_tommer > 0
    #Convert inches to centimeters
    cm = antall_tommer * 2.54
    #Return centimeters
    return cm

#Test the tommer_til_cm function
assert tommer_til_cm(1) == 2.54



#Define a procedure that incoporates and calls the previous functions
def skriv_beregninger():

    #Prompt the user for two numbers
    a = float(input("\nPlease write a number: "))
    b = float(input("Please write another number: "))

    #Use the given numbers to calcuate the addition, subtraction and division
    add = addisjon(a,b)
    sub = subtraksjon(a,b)
    div = divisjon(a,b)

    #Print the results to the terminal
    print(f"\nThe sum of the two numbers is {add:.2f}.")
    print(f"The difference of the two numbers is {sub:.2f}.")
    print(f"The quotient of the two numbers is {div:.2f}.")

    #Prompt the user for a value to convert
    a = float(input("\nWrite a number to convert from inches to centimeters: "))
    #Convert the value to centimeters
    cm = tommer_til_cm(a)
    #Print the result
    print(f'{a:.2f} inches is {cm:.2f} centimeters.\n')



#Call skriv_beregning to run the program
skriv_beregninger()