print("Hei")
print("her kommer")
print("ting på")
print("flere linjer")

print(2+3+4+5)

height = 4
length = 5
area = height * length
print(area)

print("")
pris = 4
print("one apple costs: ", pris)
print("two apple costs: ", pris*2)
print("three apple costs: ", pris*3)

#navnet = input()
#print("Velkommen", navnet)

land = input("Velg land i norde Skandinavia: ")
if land == "Norge":
    print("Oslo")
elif land == "Sverige":
    print("Stockholm")
else:
    print("fuck deg")

voksen = input("Er du voksen? y/n")
if voksen == "y":
    gravid = input("Er du gravid? y/n")
    if gravid == "y":
        print("Velkommon om bord")
    else:
        print("Du har ikke lov")
else:
    print("Du har ikke lov")