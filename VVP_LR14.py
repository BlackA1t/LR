number=int(input('Введите номер задания (1-6): '))
if number==1:
    a=int(input('Введите число A: '))
    b=int(input('Введите число B: '))
    while a<=b:
        for i in range(a):
            print(a)
        a+=1
if number==2:
    a=int(input('Введите число A: '))
    b=int(input('Введите число B: '))
    k=0
    while b<=a:
        k+=1
        a=a-b
    print('Ответ: ',k)
if number==3:
    n=int(input('Введите число N: '))
    s=0
    k=0
    while s<n:
        k+=1
        s=s+k
    print('K=',k,'S=',s)
if number==4:
    p=float(input('Введите число P: '))
    s=1000.0
    k=0
    while s<=1100:
        s=s+s*(p*0.01)
        k+=1
    print('K = ',k,'S = ',s)
if number==5:
    a=int(input('Введите число A: '))
    b=int(input('Введите число B: '))
    while a!=0 and b!=0:
        if a>b: a=a%b
        else: b=b%a
    print('Их НОД: ',a+b)
if number==6:
    n=int(input('Введите число N: '))
    f1=1
    f2=1
    f=0
    k=2
    while f<n:
        k+=1
        f=f2+f1
        f2=f1
        f1=f
    print('k = ',k)

    