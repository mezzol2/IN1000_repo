name_age = open('alder.csv')

max_age = 0
oldest = ''
for both_text in name_age:
    both_list = both_text.split(':')
    age = int(both_list[1])
    name = both_list[0]
    if age > max_age:
        max_age = age
        oldest = name


print(oldest)
