#Cats are mysterious creatures and make a variety of sounds.
#This program serves to help translate those cute little sounds into English
#Welcome to the cat translator

#Create a dictionary of cat noise
cat_dict = {
    'test' : 'very good'
}

#Define a function to return known cat "words"
def show_words():
    cat_keys = list(cat_dict.keys())
    print("\nHere is a list of known cat words.")
    print(cat_keys)

show_words()