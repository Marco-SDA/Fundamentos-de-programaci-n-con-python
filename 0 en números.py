n = int(input())
m = 0
factor = 1
while n > 0:
    r = n % 10
    n = float(n) / 10
    m = m + factor * r
    factor = factor * 100
print(m)
