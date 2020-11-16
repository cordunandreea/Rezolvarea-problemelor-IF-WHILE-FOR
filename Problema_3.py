m=int(input('introduceti un nr natural m='))
n=int(input('introduceti un nr natural n ='))
if n<m:
    print('eroare, n este mai mic ca m')
else:
    x=True
    for i in range(1,n+1):
        if m**i==n:
            print(n,'este puterea lui',m)
    x=False
    if x:
        print(n,'nu este puterea lui',m)