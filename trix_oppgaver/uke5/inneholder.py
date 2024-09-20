def inneholder(string1, string2):
    check = True
    for letter in string2:
        if letter not in string1:
            check = False
    
    return check

def inneholder2(string1, string2):
    check = True
    
    string1 = list(string1)
    string2 = list(string2)
    for i in range(len(string1)):
        for x in range(len(string2)):
            if string1[i] not in string2:
                check = False
            elif string1[i] == string2[x]:
                string1[i] = ""
                string2[x] = ""
    
    return check

def anagram(string1, string2):
    check = True

    if len(string1) != len(string2):
        check = False
    elif string1 == string2:
        check = False
    else:
        string1 = list(string1)
        string2 = list(string2)
        for i in range(len(string1)):
            for x in range(len(string2)):
                if string1[i] not in string2:
                    check = False
                elif string1[i] == string2[x]:
                    string1[i] = ""
                    string2[x] = ""

    return check


def anagram_no_work(a, b):
    if len(a) != len(b): 
        return False
    if set(a) != set(b):
        return False
    if a == b:
        return False
    return True


print(inneholder('heihei', 'hi'))

print(inneholder2('heihei', 'hei'))

print(anagram('heei', 'heii'))

print(anagram_no_work('heei', 'heii'))