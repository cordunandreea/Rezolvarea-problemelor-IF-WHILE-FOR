n=int(input('dati valoare numarului natual n='))
a=0
for i in range(1,n):
   if n%i == 0:
      a=a+i
if a==n:
   print(n,'este un numar perfect')
else:
   print(n,'nu este un numar perfect')