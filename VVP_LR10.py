number=int(input('Введите номер задания (1-7): '))
if number==1:
     a=int(input('Введите число А: '))
     b=int(input('Введите число В: '))
     if a>2 and b<=3: k=1
     else: k=0
     if k==1: print('Высказывание истинно')
     if k==0: print('Высказывание ложно')
if number==2:
     a=int(input('Введите число А: '))
     b=int(input('Введите число В: '))
     c=int(input('Введите число C: '))
     if a<b and b<c: k=1
     else: k=0
     if k==1: print('Высказывание истинно')
     if k==0: print('Высказывание ложно')
if number==3:
     a=int(input('Введите число: '))
     if a%2==0: k=1
     else: k=0
     if a>9 and a<100: c=1
     else: c=0
     if k==1 and c==1: print('Высказывание истинно')
     else: print('Высказывание ложно')
if number==4:
     a=int(input('Введите трехзначное число: '))
     k1=a//100
     k2=(a%100)//10
     k3=a%10
     if (k1<k2 and k2<k3) or (k1>k2 and k2>k3): print('Высказавание истинно')
     else: print('Высказывание ложно')
if number==5:
     a=int(input('Введите четырехзначное число: '))
     k1=a//1000
     k4=a%10
     k2=(a%1000)//100
     k3=(a%100)//10
     if k1==k4 and k2==k3: print('Высказывание истинно')
     else: print('Высказывание ложно')
if number==6:
     a=int(input('Введите число А: '))
     b=int(input('Введите число В: '))
     c=int(input('Введите число C: '))
     if (a**2+b**2==c**2) or (a**2+c**2==b**2) or (c**2+b**2==a**2): print('Высказываниеи истинно')
     else: print('Высказывание ложно')
if number==7: 
     a=int(input('Введите число А: '))
     b=int(input('Введите число В: '))
     c=int(input('Введите число C: '))
     if (a+b>c) and (a+c>b) and (b+c>a): print('Высказывание истинно')
     else: print('Высказывание ложно')



     

     
