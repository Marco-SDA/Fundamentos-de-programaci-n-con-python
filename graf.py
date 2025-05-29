import numpy as np
import matplotlib.pyplot as plt

# Datos de ejemplo
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 5, 4, 5])
n = len(x)

# Cálculo manual de la pendiente (m) y la intersección (b)
sum_x = np.sum(x)
sum_y = np.sum(y)
sum_xy = np.sum(x * y)
sum_x2 = np.sum(x**2)

m = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x**2)
b = (sum_y - m * sum_x) / n

# Predicción con la recta
y_pred = m * x + b

# Mostrar los resultados
print(f"Pendiente (m): {m:.2f}")
print(f"Intersección (b): {b:.2f}")

# Gráfica
plt.scatter(x, y, color='blue', label='Datos reales')
plt.plot(x, y_pred, color='red', label='Recta ajustada (manual)')
plt.title('Regresión Lineal Manual')
plt.xlabel('X')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()
