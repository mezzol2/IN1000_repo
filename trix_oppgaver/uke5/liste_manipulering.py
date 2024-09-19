def vanlig_konkat(list1, list2):
    list3 = list1 + list2
    return list3

def annenhver_konkat(list1, list2):
    list3 = []
    for i in range(len(list1)):
        list3.append(list1[i])
        list3.append(list2[i])
    
    return list3

def tall_til_liste(tall):
    #tall = str(tall)
    list3 = list(str(tall))
    return list3

list1 = ['a', 'b', 'c']
list2 = [1,2,3]

out = vanlig_konkat(list1, list2)
print(out)

out = annenhver_konkat(list1, list2)
print(out)

print(tall_til_liste(12))