import numpy as np

def ReduccionGaussJordan(A, calcular_inversa=False):
    # proceso para fijar la fila de referencia y hallar el factor que anula el elemento correspondiente
    filas = A.shape[0]
    
    if calcular_inversa:
        if filas != A.shape[1]:
            print("La matriz no es cuadrada, no tiene inversa")
            return None
        # Añadir matriz identidad a la derecha
        identidad = np.identity(filas)
        A = np.hstack((A, identidad))
        cols = filas * 2  # Ahora tenemos el doble de columnas
    else:
        cols = A.shape[1]

    for i in range(filas):
        # i representa la fila que está siendo fijada
        for j in range(filas):
            # j representa la fila a comparar
            if i != j:
                if A[j, i] != 0:
                    factor = (-1) * (A[i, i] / A[j, i])
                    # multiplicar fila completa en j por factor y sumar fila en i
                    filatemp = A[i, :] + (factor) * A[j, :]
                    A[j, :] = filatemp
                    
    # divir la fila completa de referencia por el valor en la diagonal para convertir en 1
    for i in range(filas):
        A[i, :] /= (A[i, i])

    if calcular_inversa:
        # Extraer la parte derecha (matriz inversa)
        inversa = A[:, filas:]
        return inversa
    else:
        return A

# Ejemplo para sistema de ecuaciones (como original)
filas = 3
matriz_ecuaciones = np.array([[3., 5., 0., 12.], 
                             [3., 6., 2., 6.], 
                             [3., 2., 1., 0.]])
print("Solución sistema ecuaciones:")
print(ReduccionGaussJordan(matriz_ecuaciones))

# Ejemplo para matriz inversa
matriz_coeficientes = np.array([[3., 5., 0.], 
                               [3., 6., 2.], 
                               [3., 2., 1.]])
print("\nMatriz inversa:")
inversa = ReduccionGaussJordan(matriz_coeficientes, calcular_inversa=True)
print(inversa)

# Verificación
print("\nVerificación (debe ser matriz identidad):")
print(np.dot(matriz_coeficientes, inversa))
