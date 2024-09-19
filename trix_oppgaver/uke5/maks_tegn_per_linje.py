def format_text(tekst, filnavn, makstegn):
    tekst = tekst.split()
    filnavn = open(filnavn, 'a')
    letters_used = 0
    for word in tekst:
        letters_used += len(word) + 1
        if letters_used-1 > makstegn:
            filnavn.write('\n')
            letters_used = len(word) + 1
            filnavn.write(f'{word} ')
        elif (letters_used-1) == makstegn:
            filnavn.write(f'{word}\n')
            letters_used = 0
        else:
            filnavn.write(f'{word} ')
        



    # while words_printed < word_count:
    #     line = ''
    #     if (words_printed + maksord) > word_count:
    #         for i in range(words_printed, word_count-1):
    #             line += (f'{tekst[i]} ')
    #         line += f'{tekst[word_count-1]}'
    #     else:
    #         for i in range(words_printed, words_printed + maksord):
    #             line += (f'{tekst[i]} ')
    #         line += f'\n'
    #     filnavn.write(line)

    #     words_printed += maksord

    filnavn.close()

format_text("I denne oppgave skal du lage et program som tar inn en tekst og skriver den ut til en fil. I utdatafilen er det maksimalt antall tegn som er tillatt per linje.",
       'test.out', 21)