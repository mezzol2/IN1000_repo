from side import Side
from firkant import Firkant

def main():
    top = Side(10, 'blue')
    assert top.get_color() == 'blue'
    assert top.get_length() == 10



main()