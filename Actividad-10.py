n = int(input("Ingrese un número entero: "))# Leer un número entero
a= 0# Inicializar los primeros términos de Fibonacci
b=1
while a <= n:# Encontrar el siguiente término después de n
    a = b
    b= a+b
print("El siguiente número en la serie de Fibonacci es:", a)# Mostrar el resultado
