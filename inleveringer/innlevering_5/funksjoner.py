#This program goes over various things that can be done with functions


#Define a function that adds two numbers together and returns the result
def adder(tall1, tall2):
    total = tall1 + tall2
    return total

#Define two numbers to add together
tall1 = 1
tall2 = 2

#Use a loop to call the fuction twice and sum tall1 and tall2
for i in range(2):
    total = adder(tall1, tall2)
    print(f'The sum of {tall1} and {tall2} is {total}.')


#Ask the user for a letter and a word
user_letter = input("Please write a single letter: ")
while len(user_letter) != 1:
    user_letter = input("Please write a single letter: ")
word = input("Please write a word: ")

#Define a function that checks how many times a letter is in a given text
def tell_forekomst(min_tekst, min_bokstav):
    #Have a loop check how many times the chosen letter is in the chosen word
    occurences = 0
    for letter in min_tekst:
        if letter == min_bokstav:
            occurences += 1
    return occurences

#Call the tell_forekomst function
occurences = tell_forekomst(word, user_letter)

#Tell the user how many times their letter shows up in their word
print(f"The letter '{user_letter}' is in '{word}' a total of {occurences} times.")
