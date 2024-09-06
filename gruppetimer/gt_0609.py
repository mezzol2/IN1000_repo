my_list = ['a', 'a','a' ]
my_set = {1, 2, 3}
my_dictionary = {
    'word' : 'ord',
    'text' : 'tekst',
    'house' : 'hus'
}

list4 = "ldskfjhsdlh"
print(len(list4))

navn = ["Ola", "Martin", "Selma"]
navn.append("Kari")
print(navn)

print(navn[1])

navn.insert(0, "Austin")
navn.insert(0, "Sally")
print(navn)

#nested lists
koffert = [
    ["tannbørste", "hårbørste", "tannkrem"],
    ["jakke", "bukse", "sokker", "undertøy"],
    ["kamera", "lommebok", "pass", "mobillader"]
]

bil = [koffert, "random shit"]
print(bil)


brukere = {}
brukere["hanjo"] = "Hanne Johnsen"
brukere["karsi"] = "Kari Sirisen"
brukere["olha"] = "Ole Hansen"

print(brukere)

brukere["karsi"] = "Kari Marie Sirisen"
print(brukere)