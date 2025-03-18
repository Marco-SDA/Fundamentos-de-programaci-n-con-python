# Solicitar entrada del usuario
n = int(input("Ingrese un número entero: "))

# Recorrer los números del 1 hasta n
for i in range(1, n + 1):
    if i % 2 == 0 and i % 3 == 0:
        print(i, "Divisible por 2 y 3")
    elif i % 3 == 0 and i % 5 == 0:
        print(i, "Divisible por 3 y 5")
    elif i % 2 == 0 and i % 5 == 0:
        print(i, "Divisible por 2 y 5")
    elif i % 2 == 0:
        print(i, "Divisible por 2")
    elif i % 3 == 0:
        print(i, "Divisible por 3")
    elif i % 5 == 0:
        print(i, "Divisible por 5")
    else:
        print(i)
