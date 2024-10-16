from side import Side
from firkant import Firkant

def main():
    top = Side(10, 'blue')
    assert top.get_color() == 'blue'
    assert top.get_length() == 10

    box = Firkant()
    assert not box.er_fullstendig()



main()