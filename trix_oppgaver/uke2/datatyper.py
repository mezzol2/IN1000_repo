streng = str(input("Write something: "))
heltall = int(input("Write a whole number:"))
flyttall = float(input("Write a decimal number: "))

print(f"{streng} is a {type(streng)}")
print(f"{heltall} is a {type(heltall)}")
print(f"{flyttall} is a {type(flyttall)}")

print(heltall * streng)
print(heltall * flyttall)
print(int(flyttall))