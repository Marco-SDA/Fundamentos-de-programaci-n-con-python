import numpy as np

def determinante_3x3(A):
    if A.shape != (3, 3):
        print("La matriz debe ser 3x3")
        return None
    
    # Expansión por cofactores (primera fila)
    det = (A[0,0]*(A[1,1]*A[2,2] - A[1,2]*A[2,1]) - 
           A[0,1]*(A[1,0]*A[2,2] - A[1,2]*A[2,0]) + 
           A[0,2]*(A[1,0]*A[2,1] - A[1,1]*A[2,0]))
    
    return det

# Ejemplo de uso
matriz = np.array([[3., 5., 0.], 
                   [3., 6., 2.], 
                   [3., 2., 1.]])

print("Matriz 3x3:")
print(matriz)

det = determinante_3x3(matriz)
print("\nDeterminante (Cofactores):", det)

# Verificación con numpy
print("Verificación con numpy:", np.linalg.det(matriz))