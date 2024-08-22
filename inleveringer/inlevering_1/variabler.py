#print a blank line for readability in the terminal
print()

#print Hei Student! to the terminal
print("Hei Student!")

#print a blank line for readability in the terminal
print()

#ask the user for their name
navn = input("Hva er navnet ditt? ")
#greet the user
print(f"Hei {navn}")

#print a blank line for readability in the terminal
print()

#define 2 integer variables
a = int(20)
b = int(11)
#print the variables on their own lines in the terminal
print(f"Den første verdien: {a}")
print(f"Den andre verdien: {b}")
#Subtract the second variable from the first print the difference
c = a - b
print(f"Differanse: {c}")

#print a blank line for readability in the terminal
print()

#ask the user for another name
navn2 = input("Hva er navnet til din beste venn? ")
#concatenate (put together) the two names and put them in 1 variable
sammen = f"{navn}{navn2}"
#print the names to the terminal
print(sammen)

#print a blank line for readability in the terminal
print()

#edit the 'sammen' variable to include ' og ' between the names
#then print the edited variable
sammen = f"{navn} og {navn2}"
print(sammen)