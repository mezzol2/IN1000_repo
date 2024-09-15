def les_song_contest(filnavn):
    årene = []
    landene = []

    for line in open(filnavn):
        line = line.strip()
        line_list = line.split()
        årene.append(line_list[0])
        landene.append(line_list[1])
    
    song_contest = {
        "år" : årene,
        "land" :landene
    }

    return song_contest

print(les_song_contest('song_contest.txt'))