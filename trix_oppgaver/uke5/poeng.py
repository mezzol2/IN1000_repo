def les_poeng(filnavn):
    poeng = {}

    for line in open(filnavn):
        line = line.strip()
        list1 = line.split(':')
        name = list1[0]
        numbers = list1[1].split(',')
        total_poeng = 0
        for i in range(len(numbers)):
            numbers[i] = int(numbers[i])
        for i in numbers:
            total_poeng += i
        poeng[name] = total_poeng
    
    return poeng
    

print(les_poeng('poeng.txt'))