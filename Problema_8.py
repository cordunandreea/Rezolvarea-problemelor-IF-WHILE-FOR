a=eval(input('nr 1='))
b=eval(input('nr 2='))
c=eval(input('nr 3='))
if a<c+b and b<c+a and c<a+b:
    if a==b and a==c and b==c:
        print('triunghiul e echilateral')
    if a==b and a+b>c :
        print('triunghiul e isoscel')
        else:
            print('triunghiul e scalen')
    else:
        print('nu poate fi format un triunghi')
