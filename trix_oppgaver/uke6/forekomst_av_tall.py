def les_tall_fra_fil(filename):
    file = open(filename, 'r')

    numbers = []
    for line in file:
        line = line.strip()
        numbers.append(line)
    file.close()

    return numbers

def antall_forekomster(list1, int1):
    count = 0
    for number in list1:
        if number == int1:
            count += 1
    
    return count

def flest_antall_forekomster(list1):

    most = list1[0]
    most_count = antall_forekomster(list1, number)

    for number in list1:
        count = antall_forekomster(list1, number)
        if count > most_count:
            most = number

    return most


file = 'tall.txt'
numbers = les_tall_fra_fil(file)
most = flest_antall_forekomster(numbers)
print(most)
