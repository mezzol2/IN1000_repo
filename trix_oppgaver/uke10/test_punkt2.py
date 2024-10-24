from punkt import Punkt

def get_user_point():
    x = float(input("x: "))
    y = float(input("y: "))
    z = float(input("z: "))
    point = Punkt(x,y,z)
    return point

def load_file_points(file_name:str):
    file = open(file_name, "r")

    point_list = []
    for line in file:
        line = line.strip()
        line = line.split(",")
        x = float(line[0])
        y = float(line[1])
        z = float(line[2])
        new_point = Punkt(x,y,z)
        point_list.append(new_point)

    file.close()

    return point_list


def main():
    #test user_point
    # print(user_point())
    
    #test load_file_points
    # points = load_file_points("gruppe1.csv")
    # for point in points:
    #     print(point)

    group1 = load_file_points('gruppe1.csv')
    group2 = load_file_points('gruppe2.csv')

    user_point = get_user_point()

    closest_points = []

    closest_points.append(user_point.faaNaermestePunkt(group1))
    closest_points.append(user_point.faaNaermestePunkt(group2))

    the_closest_point = user_point.faaNaermestePunkt(closest_points)

    print(f"\nUser point: {user_point}")
    if the_closest_point in group1:
        print(f"The closest point is {the_closest_point}, and it is in group 1.\n")
    else:
        print(f"The closest point is {the_closest_point}, and it is in group 2.\n")


main()