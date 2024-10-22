from punkt import Punkt

def main():
    point1 = Punkt(1,2,3)
    point2 = Punkt(4,5,6)
    point3 = Punkt(1,1,1)
    point4 = Punkt(1.5, 2.2, 3.3)
    point5 = Punkt(10,10,10)

    print()
    print(point1)
    print(point2)
    print()

    distnace = point1.faaAvstand(point2)
    print(f"Distance between the points: {distnace:.2f}")
    print()

    point_list = [point2, point3, point4, point5]

    closest_point = point1.faaNaermestePunkt(point_list)
    print(f"Closest Point: {closest_point}; Distance: {point1.faaAvstand(closest_point):.2f}\n")



main()