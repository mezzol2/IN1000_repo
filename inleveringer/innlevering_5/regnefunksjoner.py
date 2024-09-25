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