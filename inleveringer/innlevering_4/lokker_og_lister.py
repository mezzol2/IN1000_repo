#This program helps demonstrate the uses of loops and lists

#Make a list with a while-loo
li1 = []
i = 0
while i < 10:
    li1.append(i)
    i += 1

#Make a list with a for-loop
li2 =[]
for i in li1:
    li2.append(i)

#Question 4
#I used the list I already made (li1) with a for-loop to make li2, but I could have used the range(10)
# function to create a list.  Both li1 and range(10) contain the numbers 0 to 9.

#Create a list with multiples of 3 under 20
mine_tall = []
for i in range(0,20,3):
    mine_tall.append(i)

#Print the elements in li2 on their own lines
for i in li2:
    print(i)

#Create a list of the indicies in mine_tall
gyldige_indeksene = []
for i in range(len(mine_tall)):
    gyldige_indeksene.append(i)

#Muliply each element in mine_tall by 10
for i in gyldige_indeksene:
    mine_tall[i] *= 10

#Print the values in mine_tall
print(mine_tall)

#Question 10
#The gyldige_indeksene list is needed to iterate through the numbers in mine_tall because index
# numbers are needed to reference elements in a list.  It I had tried to use mine_tall to 
# iterate over itself, an error message would have been returned because the program would have
# tried to check index 9, and mine_tall[9] is currently undefined.