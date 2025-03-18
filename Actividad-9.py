#Serie de fibonacci
z = int(input("Ingrese el número para la serie Fibonacci: "))

a = 0
b = 1  # Primeros valores de Fibonacci

for _ in range(z + 1):  
    if a > z:  # Si el término supera z, terminamos el ciclo
        break
    print(f"{a} es parte de la sucesión hasta {z}")
    a=b
    b=a+b# Actualizamos valores

    
    
    
    
    
    
