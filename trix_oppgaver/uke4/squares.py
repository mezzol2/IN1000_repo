li = []

for x in range(5):
    li.append(x+1)

print(li)

for i in range(len(li)):
    li[i] = li[i] ** 2
    

print(li)
print(list(range(len(li))))