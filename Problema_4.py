from fractions import Fraction
m=int(input('dati numaratorul primei fractii='))
n=int(input('dati numitorul primei fractii ='))
l=int(input('dati numaratorul fractiei a doua='))
x=int(input('dati numitorul fractiei a doua='))
print('suma fractiilor=', Fraction(m,n)+Fraction(l,x))
print('produsul fractiilor=',Fraction(m,n)*Fraction(l,x))