file = open('names.txt', 'r')

personer = []
hunder = []

for line in file:
    if line[0] == 'P':
        line = line.split()
        personer.append(line[1])
    elif line[0] == 'H':
        line = line.split()
        hunder.append(line[1])

file.close()

print(personer)
print(hunder)