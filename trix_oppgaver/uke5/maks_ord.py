def format_text(tekst, filnavn, maksord):
    tekst = tekst.split()
    filnavn = open(filnavn, 'a')
    word_count = len(tekst)
    words_printed = 0

    while words_printed < word_count:
        line = ''
        if (words_printed + maksord) > word_count:
            for i in range(words_printed, word_count-1):
                line += (f'{tekst[i]} ')
            line += f'{tekst[word_count-1]}'
        else:
            for i in range(words_printed, words_printed + maksord):
                line += (f'{tekst[i]} ')
            line += f'\n'
        filnavn.write(line)

        words_printed += maksord

    filnavn.close()

format_text("I denne oppgave skal du lage et program som tar inn en tekst og skriver den ut til en fil. I utdatafilen er det maksimalt antall ord som er tillatt per linje.",
       'test.out', 5)