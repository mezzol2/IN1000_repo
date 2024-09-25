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