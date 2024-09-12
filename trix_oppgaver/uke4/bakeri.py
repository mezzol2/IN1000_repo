bakeri = {
    "Croissant" : 25,
    "Grovbroed" : 40,
    "Kneippbroed" : 20,
    "Rosinbolle" : 20,
    "Baguette" : 10
}

items = list(bakeri.keys())

def print_meny():
    print("\nVelkommen til bakeriet")
    print("\nMeny\n")


    for i in items:
        print(f"{i} : {bakeri[i]}")

print_meny()

bakeri["Croissant"] += 10

print_meny()