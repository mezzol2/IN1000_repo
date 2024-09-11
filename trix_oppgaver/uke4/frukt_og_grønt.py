beholdning = {

}

def add_product():
    run = True
    while run:
        product = input("Please enter the name of a product to add or type 'done'.\n").lower()
        if product == "done":
            run = False
        else:
            price = int(input("What is this item's price?\n"))
            beholdning[product] = price

add_product()

print("\nProducts for Sale")
for item in beholdning:
    print(f'{item} : {beholdning[item]} kr')