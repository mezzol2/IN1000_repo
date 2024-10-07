from frukt import Frukt

def main_program():
    apple = Frukt('apple', 34, True)
    #Test the class
    assert apple._navn == 'apple'
    assert apple._vann_per_100g == 34
    assert apple._spiselig == True

    pear = Frukt('pear', 56, True)
    watermelon = Frukt('watermelon', 95, True)
    trollhegg = Frukt('trollhegg', None, False)
    slyngsøtvier = Frukt('slyngsøtvier', None, False)

    fruits = [apple, pear, watermelon, trollhegg, slyngsøtvier]

    edible_water_fruits = []

    for fruit in fruits:
        if fruit._spiselig and (fruit._vann_per_100g > 85):
            edible_water_fruits.append(fruit)
    
    for fruit in edible_water_fruits:
        print(fruit.info())

main_program()