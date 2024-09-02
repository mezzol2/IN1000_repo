ordliste = ["I", "dag", "er", "jeg", "så", "lykkelig", "så", "lykkelig", "så", "lykkelig", "det", "hele", "endte", "dejligt", "jeg", "synger", "og", "er", "glad", "Ja", "alting", "endte", "lykkeligt", "så", "lykkeligt", "så", "lykkeligt", "i", "dag", "er", "jeg", "så", "lykkelig", "som", "dagen", "den", "er", "lang"]

print(len(ordliste))

print(len(set(ordliste)))

print(ordliste.count('lykkelig'))
print(ordliste.count('så'))
print(ordliste.count('dag'))

min_ordbok = {
    "lykkelig" : ordliste.count('lykkelig'),
    "så" : ordliste.count('så'),
    'dag' : ordliste.count('dag')
}

print(min_ordbok)

print(list(min_ordbok))
print(set(min_ordbok))
print(set(ordliste))