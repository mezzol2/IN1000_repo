def finn_butikk(handleliste, pris_liste, butikker):
    
    billigst = butikker[0]
    billigst_cost = 0
    for item in handleliste:
        billigst_cost += pris_liste[0][item]

    for i in range(len(pris_liste)):
        cost = 0
        for item in handleliste:
            cost += pris_liste[i][item]
        if cost < billigst_cost:
            billigst = butikker[i]
            billigst_cost = cost

    return billigst



pris_liste = [
    {"salat" : 12, "fisk" : 99, "melk" : 12, "brod" :12},
    {"salat" : 22, "fisk" : 60, "melk" : 18, "brod" :21},
    {"salat" : 8, "fisk" : 120, "melk" : 10, "brod" :19},
    {"salat" : 18, "fisk" : 40, "melk" : 30, "brod" :59},
    {"salat" : 15, "fisk" : 200, "melk" : 40, "brod" :9},
]

butikker = ["Rema1000", "Meny", "Kiwi","Spar", "Joker"]


store = finn_butikk(["fisk", "brod"], pris_liste, butikker)
print(store)