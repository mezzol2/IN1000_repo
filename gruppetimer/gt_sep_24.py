def badminton(per, palle, espen):
    if per and palle and espen:
        return False
    elif (not per) and (not palle) and (not espen):
        return False
    elif (per and palle) or (per and espen) or (palle and espen):
        return True
    else:
        return False
    
per = True
palle = False
espen = True

print(badminton(per, palle, espen))

def annen_bad(per, palle, espen):
    list1= [per, palle, espen]

    count_ja = 0

    for person in list1:
        if person == True:
            count_ja += 1
    
    if count_ja == 2:
        return True
    else:
        return False
    


def summer_rabatt(vareliste, old_prices, new_prices):
    rabatt = 0

    for item in vareliste:
        rabatt = old_prices[item] - new_prices[item]

    return rabatt


x = summer_rabatt(["laptop", "ryggsekk"], {"laptop":5000, "ryggsekk":900}, {"laptop":4000, "ryggsekk":600})
print(x)

dict1 = {"laptp":5000, "ryggsekk":900}
print(dict1)
print(list(dict1.keys()))

