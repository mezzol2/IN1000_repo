from student import Student

stud1 = Student("Joakim", 0, 0)
stud2 = Student("Kristin", 0, 0)
stud3 = Student("Dag", 0, 0)

stud_list = [stud1, stud2, stud3]

for i in range(2):
    for stud in stud_list:
        stud.legg_til_quiz_score(5)

for stud in stud_list:
    print('\n')
    stud.skriv_ut_info()
    print(f'{stud._navn}s gjennomsnittlige score er {stud.gjennomsnittlig_score()}.')