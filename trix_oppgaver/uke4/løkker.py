# for x in range(11):
#     print(x)

# i = 0
# while i <= 10:
#     print(i)
#     i += 1

#liste = ["Sauer", "er", "myke", "dyr."]
# for x in liste:
#     print(x)

# i = 0
# while i < len(liste):
#     print(liste[i])
#     i += 1

li1 = [6, -4, 7, -2, 8, -3, 9, -11]

minst = li1[0]
for num in li1:
    if num < minst:
        minst = num

print(minst)

maks = li1[0]
for num in li1:
    if num >= maks:
        maks = num

print(maks)