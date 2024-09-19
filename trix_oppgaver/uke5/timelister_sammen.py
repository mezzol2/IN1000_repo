def make_dict(file):
    work_times = {}
    file = open(file, 'r')
    
    firstline = True
    for line in file:
        if firstline:
            firstline = False
            line = line.strip()
            names = line.split(',')
            for i in names:
                work_times[i] = []
        else:
            line = line.strip()
            add_hours = line.split(',')
            for i in range(len(names)):
                hours = work_times[names[i]]
                hours.append(add_hours[i])
    file.close()
    return work_times

def combine_dict(dict1, dict2):    
    for key in dict2.keys():
        dict1[key] = dict2[key]
    return dict1

def output_file(dict1, new_filename):
    file = open(new_filename, 'w')
    line = ''
    names = list(dict1.keys())
    for key in names:
        line += f'{key},'
    line = line[:-1]
    file.write(line)

    for i in range(len(dict1[names[0]])):
        line = '\n'
        for name in names:
            line += f'{dict1[name][i]},'
        line = line[:-1]
        file.write(line)
    
    file.close()


big_dict = combine_dict(
    make_dict('timeliste1.txt'),
    make_dict('timeliste2.txt')
    )

output_file(big_dict, 'dictionary_output.txt')