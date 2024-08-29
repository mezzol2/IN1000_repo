#This program converts fahrenheit to celsius

#Set the fahrenheit temperature and print it
temp = float(input("Please enter a temperature in Fahrenheit: "))
print(f'Fahrenheit Temperature: {temp:.2f}')

#Convert the temperature to celsius and print the value
ctemp = (temp - 32) * 5/9
print(f'Celsius Temperature: {ctemp:.2f}')