brød_pris = 20
melk_pris = 15
ost_pris = 40
yoghurt_pris = 12

print("Welcome to the store.")
print("How many loafs of bread do you want?")
brød_num = int(input())

print("How many jugs of milk do you want?")
melk_num = int(input())

print("How many pieces of cheese, you fucking rat?")
ost_num = int(input())

print("How much yoghurt, you filthy animal?")
yoghurt_num = int(input())

total = brød_num*brød_pris + melk_num*melk_pris + ost_num*ost_pris + yoghurt_num*yoghurt_pris
print(f"Pay up, bitch. You owe {total} kr.")