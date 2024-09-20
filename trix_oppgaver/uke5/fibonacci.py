def finn_alle_fib_tall(tall):
    dat_list = [0, 1]
    
    if tall == 1:
        return 0
    
    for i in range(tall+1):
        new_num = dat_list[i] + dat_list[ i + 1 ]
        if new_num > tall:
            return dat_list
        else:
            dat_list.append(new_num)

def hent_tall_fra_bruker():
    inp = int(input("Write a number, you dumb whore: "))
    return inp



number = hent_tall_fra_bruker()
print(finn_alle_fib_tall(number))