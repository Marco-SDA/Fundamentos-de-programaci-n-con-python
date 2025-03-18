print("Programa que lee numeros y saca la media de los valores pares registrados.")
x=int(input("¿Cuántos números desea ingresar?\n")) #Pide la cantidad de números
suma=0
num=0
par=0
for i in range (x): #i vale 0 y se ejecuta x-1 veces numeros a ingresar
    num=int(input("Ingrese un número\n")) #El comando \n me sirve para que al ingresar un valor lo pida en un salto de línea, pues para mí se ve más entendible
    if num % 2 != 0: #Si el residuio de dividir el número en 2 no es 0, es porque es impar, entonces uso continue para ignorar dicho número
       continue
    else: #Por el contrario, si el residuo es 0, es par, entonces procedo a almacenarlo en la variable suma, y agrego 1 a la variable par, que es cuantos numeros pares encuentra
        suma+=num
        par+=1
media=suma/par #El promedio de la suma de numeros pares entre su cantidad de apariciones
print(f"La media de los números pares ingresados es: {media}") #Hago un formateo de string para imprimir media junto a la frase sin agregar la concatenación, para mí se ve más limpio así 
        
    
    
    