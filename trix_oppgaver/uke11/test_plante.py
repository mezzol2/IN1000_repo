from plante import Plante

def main():
    plant1 = Plante(40)
    plant2 = Plante(90)

    plant_list = [plant1, plant2]

    for plant in plant_list:
        plant.vann_plante(10)
    
    for plant in plant_list:
        plant.ny_dag()
    
    for plant in plant_list:
        if plant.levende():
            print("This plant is alive.")
        else:
            print("This plant is dead")



main()