from node import Node

def main():
    start = Node(0)
    current = start
    for i in range(1,5):
        neste = Node(i)
        current.nyEtterfolger(neste)
        current = neste
    
    current = start
    
    while current is not None:
        print(current.hentInnhold())
        current = current.hentNeste()

    print()

    new_node = Node(100)

    current = start

    while current.hentNeste().hentNeste() is not None:
        current = current.hentNeste()
    current.nyEtterfolger(new_node)


    current = start
    while current is not None:
        print(current.hentInnhold())
        current = current.hentNeste()

        


main()