def kalkulator():
    a = float(input("Første tall: "))
    op = str(input("Operasjon: "))
    b = float(input("Andre tall: "))
    
    def print_equ():
        print(f"{a} {op} {b} = {c}")

    if op == "+":
        c = a + b
        print_equ()
    elif op == "-":
        c = a - b
        print_equ()
    elif op == "*":
        c = a*b
        print_equ()
    elif op == "/":
        c = a/b
        print_equ()
    else:
        print("Operasjonen du skrev er ugyldig.")
        print("Vennligst prøv på nytt.")

kalkulator()