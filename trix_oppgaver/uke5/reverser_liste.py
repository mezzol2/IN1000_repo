def reverse_list(list1):

    num_items = len(list1)
    list2 = []
    for i in range(num_items, 0, -1):
        list2.append(list1[i-1])

    return list2


liste = ["en", "pluss", "to", "pluss", "tre", "er", "seks"]
print(reverse_list(liste))