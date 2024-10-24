from treNode import TreNode

def main():
    start = TreNode(3)
    assert not start.har_hoeyre_barn()
    assert not start.har_venstre_barn()

    print(start)

    start.legg_til_barn(1)
    start.legg_til_barn(4)

    assert start.har_venstre_barn()


    print(start)

    start.skriv_ut_sortert()
    print(start.hent_sorterte_list())

    assert start.søk_verdi(4)

    start.legg_til_barn(10)
    start.legg_til_barn(7)
    start.legg_til_barn(2)

    start.skriv_ut_sortert()
    assert start.søk_verdi(7)


main()