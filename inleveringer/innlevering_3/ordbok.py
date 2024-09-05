#This program shows the functionalities of dictionaries in Python

#Make a dictionary with 
my_dictionary = {
    'melk' : 14.09,
    'brød' : 24.90,
    'yoghurt' : 12.90,
    'pizza' : 39.90 
}

#Print the contents of the dictionary
print()
print(my_dictionary)

#Ask the user for a new product
prod = input("\nHvilken vare vil du legge til?\n").lower()
#Ask the user for a the product's price
price = float(input(f"Hva er prisen til {prod}?\n"))
#Add the product to the dictionary
my_dictionary[prod] = price
#Ask the user for a new product
prod = input("\nHvilken vare vil du legge til?\n").lower()
#Ask the user for a the product's price
price = float(input(f"Hva er prisen til {prod}?\n"))
#Add the product to the dictionary
my_dictionary[prod] = price

#Print the updated dictionary
print()
print(my_dictionary)
print()