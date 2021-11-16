print('Введите номер задания:')
number=int(input())
if number==1:
    print('Введите А:')
    a=int(input())
    print('Введите B:')
    b=int(input())
    x=b
    b=a
    a=x
    print('A=',a,'B=',b)
if number==2:
    print('Введите A:')
    a=int(input())
    print('Введите B:')
    b=int(input())
    print('Введите С:')
    c=int(input())
    x=b
    f=c
    b=a
    c=x
    a=f
    print('A=',a,'B=',b,'C=',c)
if number==3:
    print('Введите A:')
    a=int(input())
    print('Введите B:')
    b=int(input())
    print('Введите С:')
    c=int(input())
    x=b
    f=c
    c=a
    b=f
    a=x
    print('A=',a,'B=',b,'C=',c)
if number==4:
    print('Введите x:')
    x=int(input())
    y=(3*x**6)-(6*x**2)-7
    print('Значение функции y:',y)
if number==5:
    print('Введите x:')
    x=int(input())
    y=4*(x-3)**6-7*(x-3)**3+2
    print('Значение функции y:',y)
if number==6:
    print('Введите А:')
    a=int(input())
    x=a**2
    print('A^8=',x*x*x*x)
if number==7:
    print('Введите А:')
    a=int(input())
    x=a**2
    f=x*a
    print('A^15=',f*f*f*f*f)


