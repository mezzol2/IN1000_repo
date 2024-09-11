# x = 0
# while x < 10000:
# 	x += 1
# 	print(x)

# from random import randint

# kast_nummer = 0
# antallet_over_ti = 0
# while kast_nummer < 100000:
#     terning1 = randint(1,6)
#     terning2 = randint(1,6)

#     if terning1 + terning2 >= 10:
#         antallet_over_ti += 1

#     kast_nummer += 1

# print(antallet_over_ti)

# from random import shuffle

# dag = 0
# kopp = ['v', 'v', 'h', 'h']
# hurra = 0
# while dag < 1000:
#     shuffle(kopp)
#     linse1 = kopp[0]
#     linse2 = kopp[1]
#     if linse1 != linse2:
#         hurra += 1
#     dag += 1

# print(hurra/dag*100)

tallene = [12, 16, 5, 20]
i = 0
innenfor = True
while i < len(tallene) and innenfor == True:
    tall = tallene[i]
    if tall not in range(10,21):
        innenfor = False
    i += 1

print(innenfor)