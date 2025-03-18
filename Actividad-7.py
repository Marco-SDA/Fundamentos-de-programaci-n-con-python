positivos = 0 #Contadores
negativos = 0
suma_positivos = 0
suma_negativos = 0
while True:
    numero = int(input("Ingrese un número entero (0 para salir): "))
    if numero == 0:
        break
    elif numero > 0:
        positivos += 1
        suma_positivos += numero
    else:
        negativos += 1
        suma_negativos += numero
promedio_positivos = suma_positivos / positivos if positivos > 0 else 0 #Calcula los promedios
promedio_negativos = suma_negativos / negativos if negativos > 0 else 0
print("Cantidad de números positivos:", positivos) #Muestra los resultados
print("Promedio de números positivos:", promedio_positivos)
print("Cantidad de números negativos:", negativos)
print("Promedio de números negativos:", promedio_negativos)
