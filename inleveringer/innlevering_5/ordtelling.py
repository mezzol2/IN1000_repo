#This function takes a word as input and return the number of letters in the word
def count_letters(word):
   
    #Initialize a counting variable
    count = 0

    #Increase the count by 1 for each letter in the word
    for letter in word:
        count += 1

    return count



#This fuction takes a string and returns the frequency of each word in it
def word_frequency(text):
    
    #Split the string into words
    text = text.split()
    #Remove extra punctutaion from each word in the list
    for i in range(len(text)):
        text[i] = text[i].strip(".,?!'()")
        text[i] = text[i].strip('"')
        #make each word lowercase in order to remove case sensitivity
        text[i] = text[i].lower()

    
    #Create a dictionay
    word_count ={}

    #Add words and their frequency to the dictionary
    for word in text:
        #If the word is not in the dictionary, add it and set its frequesncy to 1
        if word not in word_count:
            word_count[word] = 1
        #If the word is in the dictionary, increase its frequency value by 1
        else:
            word_count[word] += 1
    
    #Return the dictionary
    return  word_count


#Print a line for readabilty
print('\n')

#Ask the user for a sentence
inp = input("Please write a sentence:\n")
#Get the word count of each word in the sentence
word_count = word_frequency(inp)

#Create a list of the key-values in the dictionary
keys = list(word_count.keys())

#Print a line for readabilty
print('\n')

#For each word in the list, print the word, its frequency, and how many letters it has
for word in keys:
    frequency = word_count[word]
    num_letters = count_letters(word)
    print(f'The word "{word}" appears {frequency} times and has {num_letters} letters.')

#Print a line for readabilty
print('\n')