def equals(list1, list2):

    if len(list1) != len(list2):
        return False
    
    for i in range(len(list1)):
        if list1[i] != list2[i]:
            return False
        
    return True

def same_set(list1, list2):

    for number in list2:
        if number not in list1:
            return False
        
    for number in list1:
        if number not in list2:
            return False
    
    return True

list1 = [1, 4, 9, 16, 9, 7, 4, 9, 11]
list2 = [11, 11, 7, 9, 16, 4, 1]

print(equals(list1, list2))
print(same_set(list1, list1))