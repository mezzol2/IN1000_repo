fil = open("navn.txt", 'r')

navn_liste = []

for i in fil:
    navn_liste.append(i)
fil.close()

print(navn_liste)