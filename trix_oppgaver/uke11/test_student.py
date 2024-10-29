from student import Student

def lag_ordbok():
    student1 = Student("John", "johnman", "12345")
    student2 = Student("Sarah", "sarahgirl", "09876")
    student3 = Student("Wayne", "thecowboy", "33333")

    stud_dict = {}

    stud_dict[student1.hent_navn()] = student1
    stud_dict[student2.hent_navn()] = student2
    stud_dict[student3.hent_navn()] = student3

    return stud_dict

def sjekk_student(navn, ordbok):
    if navn in ordbok.keys():
        return True
    else:
        return False

def main():
    stud_dict = lag_ordbok()
    for student in stud_dict.values():
        print(student)
    
    keep_checking = True

    while keep_checking:
        navn = input("\nWhat name do you want to check: ")
        if sjekk_student(navn, stud_dict):
            print(stud_dict[navn])
        else:
            print(f"{navn} is not in the system")
        
        inp = input("Check another? [y/n]: ").lower()
        if inp not in ['y', 'n']:
            print("Invalid input")
            inp = input("Check another? [y/n]: ").lower()

        if inp == 'n':
            keep_checking = False    


main()