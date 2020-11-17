n=int(input('varsta lui Miahi:'))
a=1
if n>20:
    print ('Mihai nu trebuie sa aiba mai mult de 20 de ani')
elif n<=20 and n>=1:
    for i in range(1,n+1):
        if (i==1):
            a=a+2
        else:
            a=(a*2)+i
print ('Mihai are ',a,' dolari')
print ('Cadoul lu Mihai a avut o valoare mai mare de 100 de dolari incepand cu varsta de 6 ani')