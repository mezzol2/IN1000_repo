def get_and_sum(tall):
    for i in range(5):
        tall.append(int(input("Write an integer: ")))

    x=0
    for i in tall:
        x += + i


    print(tall)
    print(x)

def small_list(tall):
    små_liste = []
    for i in tall:
        if i < 10:
            små_liste.append(i)

    print(små_liste)

def check_5(tall):
    five_exists = False
    i = 0
    while i < len(tall):
        if tall[i] == 5:
            five_exists = True
        i += 1 

    if five_exists:
        print("There is a five here!")
    else:
        print("No fives :(")

tall = []

get_and_sum(tall)
small_list(tall)
check_5(tall)