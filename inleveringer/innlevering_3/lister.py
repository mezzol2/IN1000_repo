#This program goes over lists and their functionalities

#First, a list is made
new_list = [2, 3, 25]
#Now, add a number to that new_list
new_list.append(29)
#Print the first and third elements of the list
print(f'\nThe first number is {new_list[0]}, and the third number is {new_list[2]}\n')

#Create a new empty list
name_list = []
#Ask the user for 4 names and add them to name_list
i = 0
while i < 4:
    name = input(f'Please add a name to the list. {4 - i} remaining: ').lower()
    name_list.append(name)
    i += 1

#Check to see if a name is in the list
name = input('\nWho do you want to check from the list?\n').lower()
if name in name_list:
    print("Du husket meg!\n")
else:
    print("Glemte du meg?\n")

#Make a new list from the sum and product of the numbers in the first list
i = 0
prod = 1
sum1 = 0
while i < len(new_list):
    sum1 += new_list[i]
    prod *= new_list[i]
    i += 1
list2 = [sum1, prod]

#Make a third list with the values of the first two lists, and print the new list
list3 = new_list + list2
print(list3)

#Remove the last two elements of the list, and print it again
list3.pop(len(list3) - 1)
list3.pop(len(list3) - 1)
print(list3)