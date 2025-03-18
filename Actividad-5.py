numero = int(input("Ingrese un número entero: ")) #Pedir un número
base = int(input("Ingrese la base (2, 4, 8 o 16): "))
if base == 2 or base == 4 or base == 8 or base == 16: #Ver si la base es válida
    resultado = ""
    while numero > 0:
        residuo = numero % base
        resultado = str(residuo) + resultado
        numero = numero // base
    print("El número convertido es:", resultado)
else:
    print("Base no válida.")
