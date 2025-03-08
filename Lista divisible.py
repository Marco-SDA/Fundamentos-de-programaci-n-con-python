def numeros_divisibles(n):
    lista = [i for i in range(n + 1) if i % 2 == 0 or i % 3 == 0 or i % 5 == 0]
    return lista

# Solicitar al usuario un valor de n
n = int(input("Ingresa un número n: "))

# Generar y mostrar la lista
print(numeros_divisibles(n))
