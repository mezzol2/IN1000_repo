def gi_største(tall1, tall2):
    if tall1 >= tall2:
        return tall1
    else:
        return tall2

def empty():
    pass

x = gi_største(2, 4)
print(x)
x = empty()
print(x)

def print_list(list1):
    for tall in list1:
        print(tall)


def laveste(list1):
    lav = list1[0]
    for i in list1:
        if i < lav:
            lav = i
    return lav

list1 = [6, 3, 2, 8, 11]

print_list(list1)
print(laveste(list1))