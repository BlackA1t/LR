number=int(input('Введите номер задания (1-5): '))
if number==1:
    c=int(input('Введите число (1-31): '))
    m=int(input('Введите месяц (1-12): '))
    if c==1: a='Первое'
    if c==2: a='Второе'
    if c==3: a='Третье'
    if c==4: a='Четвертое'
    if c==5: a='Пятое'
    if c==6: a='Шестое'
    if c==7: a='Седьмое'
    if c==8: a='Восьмое'
    if c==9: a='Девятое'
    if c==10: a='Десятое'
    if c==11: a='Одинадцатое'
    if c==12: a='Двенадцатое'
    if c==13: a='Тринадцатое'
    if c==14: a='Четырнадцатое'
    if c==15: a='Пятнадцатое'
    if c==16: a='Шестнадцатое'
    if c==17: a='Семнадцатое'
    if c==18: a='Восемнадцатое'
    if c==19: a='Девятнадцатое'
    if c==20: a='Двадцатое'
    if c==21: a='Двадцать первое'
    if c==22: a='Двадцать второе'
    if c==23: a='Двадцать третье'
    if c==24: a='Двадцать четвертое'
    if c==25: a='Двадцать пятое'
    if c==26: a='Двадцать шестое'
    if c==27: a='Двадцать седьмое'
    if c==28: a='Двадцать восьмое'
    if c==29: a='Двадцать девятое'
    if c==30: a='Тридцатое'
    if c==31: a='Тридцать первое'
    if m==1: b='января'
    if m==2: b='февраля'
    if m==3: b='марта'
    if m==4: b='апреля'
    if m==5: b='мая'
    if m==6: b='июня'
    if m==7: b='июля'
    if m==8: b='август'
    if m==9: b='сентября'
    if m==10: b='октября'
    if m==11: b='ноября'
    if m==12: b='декабря'
    print(a,b)
if number==2:
    c=str(input('Введите направление (N,S,W,E): '))
    n=int(input('Введите команду (-1/0/1): '))
    if c=='N':
        if n==-1: print('Восток')
        if n==0: print('Север')
        if n==1: print('Запад')
    if c=='S':
        if n==-1: print('Запад')
        if n==0: print('Юг')
        if n==1: print('Восток')
    if c=='W':
        if n==-1: print('Север')
        if n==0: print('Запад')
        if n==1: print('Юг')
    if c=='E':
        if n==-1: print('Юг')
        if n==0: print('Восток')
        if n==1: print('Север')
if number==3:
    c=int(input('Введите число (10-40): '))
    if c==10: print(end='Десять')
    if c==11: print(end='Одинадцать')
    if c==12: print(end='Двенадцать')
    if c==13: print(end='Тринадцать')
    if c==14: print(end='Четырнадцать')
    if c==15: print(end='Пятнадцать')
    if c==16: print(end='Шестнадцать')
    if c==17: print(end='Семнадцать')
    if c==18: print(end='Восемнадцать')
    if c==19: print(end='Девятнадцать')
    if c==20: print(end='Двадцать')
    if c==21: print(end='Двадцать одно')
    if c==22: print(end='Двадцать два')
    if c==23: print(end='Двадцать три')
    if c==24: print(end='Двадцать четыре')
    if c==25: print(end='Двадцать пять')
    if c==26: print(end='Двадцать шесть')
    if c==27: print(end='Двадцать семь')
    if c==28: print(end='Двадцать восемь')
    if c==29: print(end='Двадцать девять')
    if c==30: print(end='Тридцать')
    if c==31: print(end='Тридцать одно')
    if c==32: print(end='Тридцать два')
    if c==33: print(end='Тридцать три')
    if c==34: print(end='Тридцать четыре')
    if c==35: print(end='Тридцать пять')
    if c==36: print(end='Тридцать шесть')
    if c==37: print(end='Тридцать семь')
    if c==38: print(end='Тридцать восемь')
    if c==39: print(end='Тридцать девять')
    if c==40: print(end='Сорок')
    if (10 <= c <= 20) or (25 <= c <= 30) or (35 <= c <= 40): print(' учебных заданий')
    if c==21 or c==31: print(' учебное задание')
    if c==22 or c==23 or c==24 or c==32 or c==33 or c==34: print(' учебных задания')
if number==4:
    c=int(input('Введите число (100-999): '))
    c1=c//100
    c2=(c%100)//10
    c3=c%10
    if c1==1: print(end='сто ')
    if c1==2: print(end='двести ')
    if c1==3: print(end='триста ')
    if c1==4: print(end='четыреста ')
    if c1==5: print(end='пятьсот ')
    if c1==6: print(end='шестьсот ')
    if c1==7: print(end='семсот ')
    if c1==8: print(end='восемьсот ')
    if c1==9: print(end='девятьсот ')
    if c2==1:
        if c3==1: print('одинадцать')
        if c3==2: print('двенадцать')
        if c3==3: print('тринадцать')
        if c3==4: print('четырнадцать')
        if c3==5: print('пятнадцать')
        if c3==6: print('шестнадцать')
        if c3==7: print('семнадцать')
        if c3==8: print('восемнадцать')
        if c3==9: print('девятнадцать')
    else:
        if c2==2: print(end='двадцать ')
        if c2==3: print(end='тридцать ')
        if c2==4: print(end='сорок ')
        if c2==5: print(end='пятьдесят ')
        if c2==6: print(end='шестьдесят ')
        if c2==7: print(end='семьдесят ')
        if c2==8: print(end='восемьдесят ')
        if c2==9: print(end='девяносто ')
        if c3==2: print('два')
        if c3==3: print('три')
        if c3==4: print('четыре')
        if c3==5: print('пять')
        if c3==6: print('шесть')
        if c3==7: print('семь')
        if c3==8: print('восемь')
        if c3==9: print('девять')
if number==5:
    y=int(input('Введите год: '))
    k=y%10
    n=y%12
    f=(y+8)%12
    print(end='год ')
    if k==0 or k==1: print(end='бел')
    if k==2 or k==3: print(end='черн')
    if k==4 or k==5: print(end='зелен')
    if k==6 or k==7: print(end='красн')
    if k==8 or k==9: print(end='желт')
    if (0 <= n <= 5) or (9 <= n <= 11): print(end='ой ')
    if 6 <= n <= 8: print(end='ого ')
    if f==0: print('крысы')
    if f==1: print('коровы')
    if f==2: print('тигра')
    if f==3: print('зайца')
    if f==4: print('дракона')
    if f==5: print('змеи')
    if f==6: print('лошади')
    if f==7: print('овцы')
    if f==8: print('обезьяны')
    if f==9: print('курицы')
    if f==10: print('собаки')
    if f==11: print('свиньи')


    
    
    
