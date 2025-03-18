numero = input("Ingrese un número entero positivo: ")# Leer un número entero positivo
nuevo_numero = "" # Variable para almacenar el nuevo número
for digito in numero:# Recorrer cada cifra y sumarle 1
    nuevo_digito = (int(digito) + 1) % 10  # Si es 9, se convierte en 0
    nuevo_numero += str(nuevo_digito)
print("Número transformado:", nuevo_numero)# Muestra el resultado
