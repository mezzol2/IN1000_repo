#This program asks the user if they want a soda, and gives them
# a response depending upon their answer

#Print a blank line for readability in the terminal
print()

#Ask the user if they want a soda and save the response
#The prompt and the instructions to the user are on 2 different lines
# for better readability
print("Vil du ha en brus?")
svar = str(input("Svar ja eller nei: "))

#Print a blank line for readability in the terminal
print()

#Check the user's response
#Give the user a soda if 'svar' is 'ja'
if svar == "ja":
    print("Her har du en brus!")

#Tell the user it´s ok if they don´t want a soda
elif svar == "nei":
    print("Den er grei.")

#Tell the user that the program doesn´t understand if they
# wrote something else
else:
    print("Det forsto jeg ikke helt.")