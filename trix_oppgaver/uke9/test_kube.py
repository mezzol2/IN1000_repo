from kube import Kube

def program():
    cube1 = Kube(1,2,3)
    cube2 = Kube(3,4,5)
    cube3 = Kube(1,1,1)

    cube_list = [cube1, cube2, cube3]

    print(cube_list)
    print()
    print(sorted(cube_list))

program()