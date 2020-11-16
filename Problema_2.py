import math
n=int(input('Dati o valoare pozitiva lui n='))
suma=0
for i in range(1, n+1):
    suma+=(math.factorial(i))
print('suma =', suma)