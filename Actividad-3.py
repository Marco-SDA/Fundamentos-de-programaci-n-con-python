print("Este programa lee un número entero positivo y dice si es la raíz de otro número")
x=int(input("Ingrese un número:\n")) 
while x < 0: #Condiciona a que el número ingresado sea positivo
    x=int(input("Ingrese un entero positivo\n"))
raiz=x**(1/2) #Una raíz se puede expresar como la base elevada a 0.5 o (1/2)
if x > 0 and x%raiz == 0: #El módulo de x entre la raíz = 0 significa que sí es raíz entera
         print(f"{x} es es cuadrado de: {int(raiz)}") #Formateo de string para que sea más limpio
else:
        print(f"{x} no tiene raíz entera") 


            
        
        