number=int(input('Введите номер задания (1-5): '))
if number==1:
    s=int(input('Введите количество секунд, прошедших с начала суток: '))
    print('С начала последней минуты прошло',s-(s//60)*60,'секунд')
if number==2:
    k=int(input('Введите номер дня в года (1-365): '))
    n=k-(k//7)*7
    if n==0: print('Это воскресенье')
    if n==1: print('Это понедельник')
    if n==2: print('Это вторник')
    if n==3: print('Это среда')
    if n==4: print('Это четверг')
    if n==5: print('Это пятница')
    if n==6: print('Это суббота')
if number==3:
    k=int(input('Введите номер дня в году (1-365): '))
    n=int(input('Введите номер дня недели (1-7): '))
    f=k-(k//7)*7+n-1
    if f==7 or f==0: print('Это воскресенье')
    if f==1: print('Это понедельник')
    if f==2: print('Это вторник')
    if f==3: print('Это среда')
    if f==4: print('Это четверг')
    if f==5: print('Это пятница')
    if f==6: print('Это суббота')
if number==4:
    a=int(input('Введите длину прямоугольника: '))
    b=int(input('Введите ширину прямоугольник: '))
    c=int(input('Введите сторону квадрата: '))
    s=a*b
    k=s//(c**2)
    n=s-k*(c**2)
    print('В прямоугольнике поместиться',k,'квадратов, и останется',n,'ед. незанятой площади')
if number==5:
    n=int(input('Введите номер года: '))
    s=(n-1)//100+1
    print('Этого год относиться к',s,'столетию')


