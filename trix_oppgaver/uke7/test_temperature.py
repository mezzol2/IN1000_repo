from temperatur import Temperatur

def hovedprogram():
    temp = float(input("Write a temperature: "))
    scale = input("Specify scale: ")

    temp_converter = Temperatur(temp, scale)

    print(f"{temp_converter._c:.2f} C")
    print(f"{temp_converter._f:.2f} F")
    print(f"{temp_converter._k:.2f} K")

hovedprogram()