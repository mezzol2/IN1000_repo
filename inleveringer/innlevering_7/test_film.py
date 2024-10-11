from film import Film

def test_film():
    # __init__
    # Opprett to film-objekter med tittel og produksjonsår du velger selv
    print("\nOppretter to filmer\n")
    # <fyll ut og fjern # på print-setningen>
    movie1 = Film('Fight Club', 1999)
    movie2 = Film('Star Wars', 1977)

    # hent_tittel
    # Skriv ut tittel på de to filmene
    print("Skriver ut titler på to filmer")
    # <fyll ut og fjern # på print-setningen>
    print(movie1.hent_tittel())
    print(movie2.hent_tittel())
    print()

    # ny_skuespiller
    # Legg til to skuespillere og deres roller for en av filmene, skriv ut alt om filmen
    print("Legger til to skuespillere")
    # <fyll ut og fjern # på print-setningen>
    movie1.ny_skuespiller("Brad Pitt", "Tyler Durdan")
    movie1.ny_skuespiller("Edward Norton", "The Narrator")
    movie1.skriv_ut_film()
    print()

    # Prøv å legge inn en av skuespillerne igjen, med en ny rolle, og sjekk at rollen ikke blir endret
    print("Tester ulovlig innlegging av skuespiller")
    # <fyll ut og fjern # på print-setningen>
    movie1.ny_skuespiller("Edward Norton", "Jack")
    print()

    # skriv_ut_film
    # Skriv ut all informasjon om begge filmer du har lagt inn
    print("Skriver ut all info om to filmer:")
    # <fyll ut og fjern # på print-setningen>
    movie1.skriv_ut_film()
    movie2.skriv_ut_film()
    print()

    # hent_alle_skuespiller_navn
    # Skriv ut skuespillernes navn for den filmen som har to
    print("Henter og skriver ut alle skuespillernavn for en film:")
    # <fyll ut og fjern # på print-setningen>
    actor_list = movie1.hent_skuespiller_navn()
    print(f"\nSkuespillere i {movie1._tittel}:")
    for actor in actor_list:
        print(actor)
    print()

    # sjekk_periode
    # Sjekk om en film du har lagt inn er i en periode du velger
    # (velg periode som skal gi True og sjekk at dette blir resultatet)
    print ("Sjekker at en film er i oppgitt periode")
    # <fyll ut og fjern # på print-setningen>
    assert movie1.sjekk_periode(1995, 2005)

    # Sjekk om en film er i en periode som skal gi False
    # (velg samme årstall til begge argumenter og sjekk resultat er False)
    print ("Sjekker at en film ikke kan være produsert før og etter samme år")
    # <fyll ut og fjern # på print-setningen>
    assert not movie1.sjekk_periode(1999,1999)

    # sjekk_tittel
    # Sjekk om en film har en tittel som starter på en streng som du selv velger
    print ("Sjekker om starten på en films tittel kjennes igjen")
    # <fyll ut og fjern # på print-setningen>
    assert movie1.sjekk_tittel("Fight")

test_film()