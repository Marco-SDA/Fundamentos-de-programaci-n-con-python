# Solicitar entrada al usuario
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

# Verificar si son ambos pares o impares
if (num1 % 2 == num2 % 2):  # Ambos pares o ambos impares
    while num2 != 0:
        resto = num1 % num2
        num1 = num2
        num2 = resto  # Algoritmo de Euclides para el MCD
    print("El máximo común divisor es:", num1)
else:
    # Calcular el mínimo común múltiplo (MCM)
    producto = num1 * num2
    while num2 != 0:
        resto = num1 % num2
        num1 = num2
        num2 = resto  # Algoritmo de Euclides para MCD
    print("El mínimo común múltiplo es:", producto // num1)  # MCM = (num1 * num2) / MCD
