numero = int(input("Ingrese un número"))
binario = ""
decimal = 0

while numero > 0:
    if numero % 2 == 0:
        binario =  "0" + binario
    else:
        binario =  "1" + binario
    numero = numero // 2 
print(binario)

decimal = 0
pos = len(binario)
for i in reversed(binario):
    if i == "1":
        decimal = decimal + pow(2, (len(binario)-pos))
    pos = pos-1
print(decimal)