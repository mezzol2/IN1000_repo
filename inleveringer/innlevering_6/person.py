#Define a class Person with instance variables name, age, and hobbies.
# This class will have methods to add a new hobby to the hobbies list.
# The class will also have a method to print out all the hobbies, and one
# print all the information on the person.

#Define class Person
class Person:
    #Define the constructor and its parameters
    def __init__(self, name:str, age:int) -> None:
        #Define instance variables for name and age
        self._name = name
        self._age = age
        #Define hobbies as an empty list
        self._hobbies = []
    
    #Define a method that adds a given hobby to the hobbies list
    def add_hobby(self, new_hobby):
        self._hobbies.append(new_hobby)
    
    #Define a method that prints the hobbies list in a readable format
    def print_hobbies(self):
        #Check how many hobbies the person has, and format the message accordingly
        #If the person has no hobbies, print a message stating as much
        if len(self._hobbies) == 0:
            print(f"{self._name} appears to have no hobbies.  What a square.\n")
        #If the person has 1 hobby, state that it is their only hobby.
        elif len(self._hobbies) == 1:
            print(f"{self._name}'s only hobby is {self._hobbies[0]}.\n")
        else:
            #Create a string with the person's hobbies
            hobby_string = ""
            for i in range(len(self._hobbies)-1):
                hobby_string += f"{self._hobbies[i]}, "
            hobby_string += f"and {self._hobbies[-1]}"
            #Print a readable version of the hobbies
            print(f"{self._name}'s hobbies are {hobby_string}.\n")
    
    #Define a method that prints all the person's info
    def print_all(self):
        print(f"\n{self._name} is {self._age} years old.")
        self.print_hobbies()
        