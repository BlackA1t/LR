number=int(input('Введите номер задания (1-5): '))
if number==1:
    def powera3(a): return a**3
    for i in range(5): 
        a=float(input('Введите число: '))
        b=powera3(a)
        print('Куб этого числа: ',b)
if number==2:
    def sign(x):
        if x<0: return -1
        if x==0: 0
        if x>0: return 1
    a=float(input('Введите число A: '))
    b=float(input('Введите число B: '))
    print('Ответ: ', sign(a)+sign(b))
if number==3:
    def rings(r1,r2): return 3.14*r1*r1 - 3.14*r2*r2
    for i in range(3):
        r1=float(input('Введите первый радиус: '))
        r2=float(input('Введите второй радиус: '))
        print('Площадь кольца: ',rings(r1,r2))
if number==4:
    def quarter(x,y):
        if x>0 and y>0: return 'Первая четверть'
        if x<0 and y>0: return 'Вторая четверть'
        if x<0 and y<0: return 'Третья четверть'
        if x>0 and y<0: return 'Четвертая четверть'
    for i in range(3):
        x=float(input('Введите координату Х: '))
        y=float(input('Введите координату Y: '))
        print(quarter(x,y))
if number==5:
    def fact2(n):
        k=1
        if n%2==0: 
            i=2
            while i<=n:
                k=k*i
                i+=2
        else:
            i=1
            while i<=n:
                k=k*i
                i+=2
        return k
    n=int(input('Введите число: '))
    print('Его двойной факториал: ',fact2(n))
                



        



