number=int(input('Введите номер задания (1-5): '))
if number==1:
    a=float(input('Введите цену 1 кг конфет: '))
    print('Стоимость 0.1 кг: ',"%.2f" % (a*0.1))
    print('Стоимость 0.2 кг: ',"%.2f" % (a*0.2))
    print('Стоимость 0.3 кг: ',"%.2f" % (a*0.3))
    print('Стоимость 0.4 кг: ',"%.2f" % (a*0.4))
    print('Стоимость 0.5 кг: ',"%.2f" % (a*0.5))
    print('Стоимость 0.6 кг: ',"%.2f" % (a*0.6))
    print('Стоимость 0.7 кг: ',"%.2f" % (a*0.7))
    print('Стоимость 0.8 кг: ',"%.2f" % (a*0.8))
    print('Стоимость 0.9 кг: ',"%.2f" % (a*0.9))
    print('Стоимость 1 кг: ',a)
if number==2:
    n=int(input('Введите число: '))
    a=1.1
    for i in range(n-1):
        a=a*(1+0.1*(i+2))
    print('Ответ: ',"%.3f" % a)
if number==3:
    n=int(input('Введите число: '))
    a=0
    i=1
    while i <= (2*n-1):
        a+=i
        i+=2
    print('Квадрат этого числа: ',a)
if number==4:
    a=float(input('Введите число A: '))
    n=int(input('Введите число N: '))
    i=1
    s=1
    while i<=n:
        s=s+(a**i)
        i+=1
    print('Ответ: ',s)
if number==5:
    a=float(input('Введите число A: '))
    n=int(input('Введите число N: '))
    s=0
    for i in range(n+1): s=s+(-a)**i
    print('Ответ: ',s)









