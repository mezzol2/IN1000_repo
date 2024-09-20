def omvendt_fil(input_filnavn, output_filnavn):
    file = open(input_filnavn, 'r')
    lines = []
    for line in file:
        lines.append(line.strip())

    file.close()
    reversed_lines = lines[::-1]

    file = open(output_filnavn, 'w')
    for line in reversed_lines:
        file.write(f'{line}\n')

    
    file.close()



omvendt_fil('input.txt', 'reversed.txt')