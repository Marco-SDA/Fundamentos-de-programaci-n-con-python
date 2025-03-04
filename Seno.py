angulo = int(input())
x = angulo * 3.14159 / 180
n = int(input())
suma = 0
for i in range(0, n + 1, 1):
    fact = 1
    kmax = 2 * i + 1
    for k in range(1, kmax + 1, 1):
        fact = fact * k
    suma = suma + (-1) ** i * x ** (2 * i + 1) / fact
print(suma)
