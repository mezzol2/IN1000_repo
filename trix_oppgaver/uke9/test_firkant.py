from side import Side
from firkant import Firkant

def sjekk_firkanter(shape_list):
    for shape in shape_list:
        if not shape.er_fullstendig():
            return False
    return True

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

    box.fjern_side('l')
    assert not box.er_fullstendig()

    #make one more box
    box1 = Firkant()
    box1.legg_til_side(top, 't')
    box1.legg_til_side(bottom, 'b')
    box1.legg_til_side(left, 'l')
    box1.legg_til_side(right, 'r')

    #Test the sjekk_firkanter method
    box_list = [box1]
    assert sjekk_firkanter(box_list)
    
    box_list.append(box)
    assert not sjekk_firkanter(box_list)


main()