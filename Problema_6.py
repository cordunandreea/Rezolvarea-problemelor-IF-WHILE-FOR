n=int(input('n='))
s1=0
s2=0
s3=0
s4=0
c=n
for i in range(1,n+1):
    s1=s1+(i**3)
    s2=s2+i
s2a=s2**2
if(s2a>s1):
    print('s2 este mai mare')
elif(s2a==s1):
    print('suma s1 este egala cu suma s2')
elif s1>s2a:
    print('s1 este mai mare')

for j in range(1,p+1):
    s3=s3+(i**2)
    s4=s4+i
s3a=s3*3
s4a=s4+(n**3)+(n**2)
if s4a>s3a:
    print('s2 este mai mare')
elif s3a==s4a:
    print('suma s1 si su ma s2 sunt egale')
elif s3a>s4a:
    print('s1 este mai mare')