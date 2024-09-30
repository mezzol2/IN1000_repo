from rektangel import Rektangel

a = 7
b = 2

rect = Rektangel(a,b)
print(rect.areal())
print(rect.omkrets())

a = 1
b = 2
rect2 = Rektangel(a,b)
print(rect2.areal())
print(rect2.omkrets())

rect2.oekLengde(1)
rect2.oekBredde(1)
print(rect2.areal())
print(rect2.omkrets())

rect2.reduserLengde(100)