def sorter_etter_karakter(filnavn):
    file = open(filnavn, 'r')

    grade_dict = {}
    

    for line in file:
        line = line.strip()
        line = line.split(',')
        if line[1] not in grade_dict:
            new_list = []
            new_list.append(line[0])
            grade_dict[line[1]] = new_list
        else:
            grade = line[1]
            new_list = grade_dict[grade]
            new_list.append(line[0])
        
    file.close()

    return grade_dict

def skrive_ut_sortert(grade_dict):
    
    for key in sorted(grade_dict.keys()):
        print(f'{key} : {grade_dict[key]}')

def hent_vanligste_karakter(grade_dict):
    l = 0
    for grade in grade_dict:
        if len(grade_dict[grade]) > l:
            vanligste = grade
            l = len(grade_dict[grade])
    

    return vanligste


grade_dict = sorter_etter_karakter('karakter.csv')
skrive_ut_sortert(grade_dict)
print(hent_vanligste_karakter(grade_dict))
