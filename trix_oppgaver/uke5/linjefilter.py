def fil_na_filter(input_fil_navn, output_fil_navn):
    input_fil = open(input_fil_navn, 'r')
    ouput_fil = open(output_fil_navn, 'a')

    for linje in input_fil:
        if 'NA' not in linje:
            ouput_fil.write(linje)
    
    input_fil.close()
    ouput_fil.close()


fil_na_filter("input_med_na.csv", "output_uten_na.csv")



