from dag import Dag

def les_inn_fil(filename:str):
    dag_liste = []
    file = open(filename, 'r')
    
    for line in file:
        line = line.strip()
        line = line.split('-')
        for part in line:
            part = part.strip()
        dato = line[0]
        line[1] = line[1].split()
        line[1][0] = line[1][0].replace(',', '.')
        nedbørtall = float(line[1][0])
        dag = Dag(dato, nedbørtall)
        dag_liste.append(dag)

    file.close()
    return dag_liste

def maksdag(dag_liste:list):
    maks_dag = dag_liste[0]
    for dag in dag_liste:
        if dag.get_nedbørtall() > maks_dag.get_nedbørtall():
            maks_dag = dag
    
    return maks_dag

def til_sammen(dag_list:list):
    total_regn = 0
    for dag in dag_list:
        total_regn += dag.get_nedbørtall()
    
    return total_regn


def main():
    filename = "Nedbørsmengder.txt"
    daglig_data = les_inn_fil(filename)

    print(daglig_data[0].get_date())
    print(daglig_data[0].get_nedbørtall())
    
    most_rainy_day = maksdag(daglig_data)
    print(most_rainy_day)

    total_regn = til_sammen(daglig_data)
    print(f"Total rain: {total_regn:.1f} mm")

main()