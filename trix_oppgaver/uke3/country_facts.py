country = {
    'capital' : {
        'Norway' : 'Oslo',
        'Sweden' : 'Stockholm',
        'Denmark' : 'Copenhagen'
    },

    'language' : {
        'Norway' : 'Norwegian',
        'Sweden' : 'Swedish',
        'Denmark' : 'Danish'
    },

    'population' : {
        'Norway' : 5457000,
        'Sweden' : 10490000,
        'Denmark' : 5903000
    }
}

land = input("Please write a country name: ")

if (land == 'Norway') or (land == 'Sweden') or (land == 'Denmark'):
    print(country['capital'][land])
    print(country['language'][land])
    print(country['population'][land])
else:  
    print("Please enter a REAL country.")
