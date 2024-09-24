def skriv_med_trykk(text):
    text += '!'
    
    return text
inp = input("Give me a word: ")
while inp.lower() != 'nei':

    print(skriv_med_trykk(inp))
    inp = input("Give me a word: ")