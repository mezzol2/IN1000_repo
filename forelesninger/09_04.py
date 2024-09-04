my_list = []

i = 0

while i < 5: 
    new_num = int(input("Add a number to the list: "))
    my_list.append(new_num)
    i += 1

print(my_list)
print(my_list.count(4) * 4)

my_set = set(my_list)

if len(my_set) == 1:
    print("Yahztee!!")
elif len(my_set) == 2:
    if my_list.count(my_list[0]) in [2,3]:
        print("you have a full house")
else:
    print("no yahtzee...\n")


capital = {
    "norge" : "Oslo",
    "sverige" : "Stockholm"
}
land = input().lower()
print(capital[land])

table = [[5,3],
         [3,5]]
rad1 = table[0][0]
rad2 = table[1][0]
kol1 = table[0][1]
kol2 = table[1][1]
all_like = rad1 == rad2 == kol1 == kol2
print(all_like)