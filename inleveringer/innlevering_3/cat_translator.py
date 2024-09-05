#Cats are mysterious creatures and make a variety of sounds.
#This program serves to help translate those cute little sounds into English
#Welcome to the cat translator

#Create a dictionary of cat noise
cat_words = {
    'mew' : "Look at me, I'm a kitten.",
    'meow' : "Notice me!",
    'MEOWWW' : "Dinner is 30 seconds late, and I am dissatisfied, human.",
    'purr' : "I am content with the current situation.",
    'ekekekkekkek' : "Mother, I crave violence.",
    'growl' : "Unhand me. I do not consent to this.",
    '*stares silently*' : "The cat is attempting to communicate telepathically. Try listening."
}

#Define a function to return known cat "words"
def show_words():
    cat_keys = list(cat_words.keys())
    print("\nHere is a list of known cat words.")
    print(cat_keys)
    print()

#Greet the user
print("\nHello, human.  Welcome to the cat translator.")
#Ask the user if the need to see known cat words
inp = input("Do you need to see the list of translatable cat words?\n[y/n] ").lower()
#Show the user the list if they want it
if inp == 'y':
    show_words()

#Ask the user if they want to translate a word
inp = input("\nWould you like to translate a cat word?\n[y/n?] ").lower()
#If the user wants a translation, ask them for a word
if inp == 'y':
    inp = input("\nWhat word do you need translated: ")
    #If the user's word is in the cat_word dictionary, print the translation
    if inp in cat_words:
        print(f'\n{cat_words[inp]}\n')
    
    #If the user's word is not in cat_word, tell the user
    else:
        print("That word is not in the dictionary. Please try again.")

#If the user does not want a translation, send them on their way    
elif inp == 'n':
    print("\nGuess you speak fluent cat already. BYE.\n")

#If the user gave an invalid reponse, mock them
else:
    print("It's a yes or no question. Why are you making this hard?\n")