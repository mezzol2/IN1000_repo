def to_stoerste_tall(liste):
    tall1 = 0
    tall2 = 0

    for tall in liste:
        if tall > tall1:
            tall2 = tall1
            tall1 = tall
        elif tall > tall2:
            tall2 = tall

    return [tall1, tall2]

list1 = [2, 3, 982734, 11, -22123, 23047987,1111111]

print(to_stoerste_tall(list1))

def format_navn(fullt_navn):
    formatted_name =''

    for navn in fullt_navn.split():
        navn = navn[0].upper() + navn[1:]
        formatted_name += navn + ' '

    formatted_name = formatted_name.strip()   

    return formatted_name

letter = format_navn('austin moore')
print(letter)
assert letter == 'Austin Moore'