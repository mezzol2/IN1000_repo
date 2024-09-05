def get_rgb():
    rgb_inp = input('Sup, dog? Give me an RGB color: ')
    rgb = rgb_inp.split()
    
    if len(rgb) != 3:
        exit("Dude. You didn't give me three numbers.  WTF?")
    else:
        i = 0
        while i < 3:
            rgb[i] = int(rgb[i])
            i += 1
    
    i = 0
    while i < 3:
        if rgb[i] < 0 or rgb[i] >= 256:
            print(f'Bruh.  {rgb} has at least one value outside the acceptble range of 0 to 255.')
            exit(f'Stop this tom-foolery and try again.')
        i += 1
        
    print(f'{rgb} is a fine color.')


get_rgb()