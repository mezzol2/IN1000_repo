telefonbok = {
    "Arne"  : 22334455,
    "Lisa"  : 95959595,
    "Jonas" : 97959795,
    "Peder" : 12345678
}

navn = input("Whose number would you like to check?\n")

if navn in telefonbok:
    print(telefonbok[navn])
else:
    action = input("That name is not in the telephone book\nWould you like to add it now?[y/n] ")
    if action == "y":
        new_num = int(input(f"Please enter {navn}'s phone number.\n"))
        telefonbok[navn] = new_num
    else:
        print("Goodbye.")

print("")
print(telefonbok)