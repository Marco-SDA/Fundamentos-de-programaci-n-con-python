numero = int(input("Ingrese un número entero mayor que 2:\n"))# Pedir un número 

if numero <= 2:
    print("El número debe ser mayor que 2.")
else:
    while True:
        es_primo = True
        for i in range(2, numero):  # Verifica desde 2 hasta el número - 1
            if numero % i == 0:
                es_primo = False
                break
        
        if es_primo:
            print(f"El número primo más cercano es: {numero}")
            break
        
        numero -= 1 #Si no es primo, se prueba con el número anterior



   
    
     
        

        