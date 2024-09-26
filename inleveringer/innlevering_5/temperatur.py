#This program calls reads two files with temperature data.  One file was monthly
# temperature records and the other has daily temperatures for 2018.  The program
# will print a message if it finds a new highest monthly record.

#Define a function that returns the contents of a file with 2 columns
#Here, the file has monthly temperature info
def month_temp(filename):
    #Open the file as read-only
    file = open(filename, 'r')

    #Define an empty dictionary and add the file information to it
    temp_dict = {}
    for line in file:
        #Remove line breaks
        line = line.strip()
        #Split the line into sperate elements
        line = line.split(',')
        #Add the information to the dictionary
        temp_dict[line[0]] = float(line[1])

    #Close the file
    file.close()

    #Return the dictionary
    return temp_dict



#Call the month_temp fuction and print the results
max_temp_per_month = month_temp('max_temperatures_per_month.csv')
print(max_temp_per_month)



#Define a function that prints a message if there is a new temperature record
#This function uses a dictionary and external file as inputs
def daily_temps(temp_dict, filename):
    #Open the file
    file = open(filename, 'r')

    #Iterate each line in the file
    for line in file:
        #Format the line
        line = line.strip()
        line = line.split(',')
        #Check if the daily temperature is greater than the previous record
        if float(line[2]) > temp_dict[line[0]]:
            #Format variables for readability
            new_temp = float(line[2])
            old_temp = temp_dict[line[0]]
            month = line[0]
            day = line[1]
            #Print a message if there is a record
            print(f'\nWow! {new_temp} degrees from {month} {day} is the new temperature record!')
            print(f'The previous record for {month} was {old_temp}')

            #Update the dictionary with the new temperature records
            temp_dict[month] = new_temp

    #Close the file
    file.close()

    #Print line for readabilty
    print()

    #Return the temperature dictionary
    return temp_dict


#Call the daily_temps function and update the the dictionary
max_temp_per_month = daily_temps(max_temp_per_month, 'max_daily_temperature_2018.csv')
#Print the updated records
print(max_temp_per_month)