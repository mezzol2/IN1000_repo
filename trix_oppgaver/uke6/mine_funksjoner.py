def lengde(item):
    
    count = 0
    for i in item:
        count += 1

    return count

item = ['hello', 2, 4, 6]

print(lengde(item))

def tell(string, letter):

    i = 0
    for letters in string:
        if letter == letters:
            i += 1

    return i

print(str.count('word', 'o'))
print(tell('word', 'o'))

# def tell2(list1, sublist):

#     count = 0
#     for i in range(len(list1)):
#         if sublist[0] == list1[i]:
#             count += 1
#             for n in range(len(sublist)):
#                 if (i+n+1) > len(list1):
#                     count -= 1
#                     break
#                 elif sublist[n] != list1[i + n]:
#                     count -= 1
#                     break

#     return count

def tell2(string1, substring):
    count = 0
    string1 = list(string1)
    substring = list(substring)

    for i in range(len(string1)):
        end = i + len(substring)

        if string1[i:end] == substring:
            count += 1
            for n in range(len(substring)):
                string1[i+n] = ""
    
    return count


print(tell2("hellolll", "ll"))

def range_liste(start, end):
    list1 =[]
    while start < end:
        list1.append(start)
        start += 1

    return list1

print(range_liste(2,10))
print(range(2,10))