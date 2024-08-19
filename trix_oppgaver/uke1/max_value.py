value1 = int(input("Enter the first value: "))
value2 = int(input("Enter the second value: "))
value3 = int(input("Enter the last value: "))

if value1 >= value2 and value1 >= value3:
    maxvalue = value1
elif value2 >= value1 and value2 >= value3:
    maxvalue = value2
else:
    maxvalue = value3
    


print("")
print(f'First number {value1}')
print(f'Second number {value2}')
print(f'Third number {value3}')
print(f'Highest number {maxvalue}')