number=int(input('Введите номер задания (1-6): '))
if number==1:
    a=int(input('Введите число А: '))
    b=int(input('Введите число В: '))
    if a==b:
        a=0
        b=0
    else:
        if a>b: b=a
        if b>a: a=b
    print('A=',a,'B=',b)
if number==2:
    a=int(input('Введите число А: '))
    b=int(input('Введите число В: '))
    c=int(input('Введите число C: '))
    if a>b and a>c: 
        k=a
        if b>c: k=k+b
        else: k=k+c
    if b>a and b>c: 
        k=b
        if a>c: k=k+a
        else: k=k+c
    if c>a and c>b: 
        k=c
        if a>b: k=k+a
        else: k=k+b
    if a==b and b==c:
        k=a+b
    print('Сумма двух наибольших из них: ',k)
if number==3:
    a=int(input('Введите число А: '))
    b=int(input('Введите число В: '))
    c=int(input('Введите число C: '))
    rb=abs(a-b)
    rc=abs(a-c)
    if rb>rc: print('Расстояние от точки А до точки B: ',rb)
    if rc>rb: print('Расстояние от точки А до точки C: ',rc)
    if rb==rc: print('Расстояния от точек В и С до точки А одинаковое')
if number==4:
    print('Введите координаты точки (XY): ')
    x=int(input())
    y=int(input())
    if x>0 and y>0: print('Точка принадлежит первой четверти')
    if x<0 and y>0: print('Точка принадлежит второй четверти')
    if x<0 and y<0: print('Точка принадлежит третьей четверти')
    if x>0 and y<0: print('Точка принадлежит четвертой четверти')
if number==5:
    a=int(input('Введите число: '))
    print('Это число ')
    if a==0: print('нулевое')
    else:
        if a>0: print('положительное')
        if a<0: print('отрицательное')
        if a%2==0: print('четное')
        else: print('нечетное')
if number==6: 
    a=int(input('Введите число (1-999): '))
    print('Это число')
    if a%2==0: print('четное')
    else: print('нечетное')
    if a<10: print('однозначное')
    else:
        if a<100: print('двузначное')
        else: print('трехзначное')



    
    
    