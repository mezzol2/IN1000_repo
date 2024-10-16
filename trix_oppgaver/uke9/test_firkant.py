from side import Side
from firkant import Firkant

def main():
    top = Side(10, 'blue')
    assert top.get_color() == 'blue'
    assert top.get_length() == 10

    box = Firkant()
    assert not box.er_fullstendig()

    bottom = Side(2, 'red')
    left = Side(5, 'green')
    right = Side(7, 'yellow')

    box.legg_til_side(top, 't')
    box.legg_til_side(bottom, 'b')
    box.legg_til_side(left, 'l')
    box.legg_til_side(right, 'r')

    assert box.er_fullstendig()

main()