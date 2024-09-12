#This program will ask the user for numbers, and then determine the
# largest and smallest numbers given

#Initize a variable and a list to be used in a while loop
number = 1
num_list =[]

#Ask the user for numbers until they give a 0
while number != 0:
    number = float(input("Write a number: "))
    if number != 0:    
        num_list.append(number)

#Prepare a string of the numbers to print
num_string = ""
for num in num_list:
    num_string += f" {num},"


#Print the numbers that the user input
print(f"Your numbers are:{num_string[:-1]}")

#Sum togther the values in the list
min_sum = 0
for x in num_list:
    min_sum += x

#Print the sum
print(f'The sum of the values is {min_sum}.')

#Find the minimum value
minimum = num_list[0]
for num in num_list:
    if num < minimum:
        minimum = num

#Return the value to the user
print(f"The smallest number is {minimum}.")

#Find the maximum value
maximum = num_list[0]
for num in num_list:
    if num > maximum:
        maximum = num

#Return the value to the user
print(f"The largest number is {maximum}.")