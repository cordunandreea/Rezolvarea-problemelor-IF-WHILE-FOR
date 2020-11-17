n=int(input('n='))
a=0
for i in range(1,n):
    s1a=a+(i**3)
    s2a=a+i
sa2a=s2a**2
if sa2a>s1a:
    print('a)a doua suma este mai mare')
elif sa2a==s1a:
    print('a)ambele sume sunt egale')
elif s1a>sa2a:
    print('a)prima suma este mai mare')

for i in range(1,n):
    s1b=a+(i**2)
    s2b=a+i
sb1b=s1b*3
sb2b=s2b+(n**3)+(n**2)
if sb2b>sb1b:
    print('b)a doua suma este mai mare')
elif sb1b==sb2b:
    print('b)ambele sume sunt egale')
elif sb1b>sb2b:
    print('b)prima suma este mai mare')