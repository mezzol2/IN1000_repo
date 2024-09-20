def oppskrift_fra_sukker(sukker):

    ingredienser = {
        'sukker' : sukker,
        'mel' : sukker * 2,
        'smør' : sukker * 3
    }

    return ingredienser

def skriv_oppskrift(sukker, mel, smør):
    print(f'Since you have {sukker} pounds sugar,')
    print(f'go get your bitch-ass like {mel} pounds of flour.')
    print(f'Try not to forget the butter, dumbass.\nYou need {smør} pounds of that.')
    print("Then you can make some goddamn cake.")

def bak_kaker():
    inp = int(input("How much sugar you got?\n"))
    return inp

number = bak_kaker()
stuff_you_need = oppskrift_fra_sukker(number)
skriv_oppskrift(stuff_you_need['sukker'], stuff_you_need['mel'], stuff_you_need['smør'])
