number=int(input('Введите номер задания (1-5): '))
if number==1:
    n=int(input('Введите число N: '))
    m=[0]*n
    k=1
    for i in range(n):
        m[i]=k
        k+=2
    for i in m:
        print(i)
if number==2:
    n=int(input('Введите число N: '))
    a=int(input('Введите число A: '))
    d=int(input('Введите число D: '))
    m=[0]*n
    k=0
    for i in range(n):
        m[i]=a*d**k
        k+=1
    for i in m:
        print(i)
if number==3:
    n=int(input('Введите число N: '))
    a=int(input('Введите число A: '))
    b=int(input('Введите число B: '))
    m=[0]*n
    m[0]=a
    m[1]=b
    i=2
    while i<n:
        for j in range(i):
            m[i]+=m[j]
        i+=1
    for i in m:
        print(i)
if number==4:
    n=int(input('Введите число N: '))
    a=[0]*n
    m=[0]*n
    for i in range(n):
        a[i]=i
    i=1
    k=0
    while i<n:
        if i%2==0:
            m[i]=a[i]
        else:
            m[i]=a[n-1-k]
        i+=1
        k+=1
    for i in m:
        print(i)
if number==5:
    n=int(input('Введите число N: '))
    a=[0]*n
    m=[0]*n
    for i in range(n):
        a[i]=i
    i=0
    k=0
    f=1
    while i<n:
        if i%2!=0:
            m[k]=a[i]
            k+=1
        else:
            m[n-f]=a[i]
            f+=1
        i+=1        
    for i in m:
        print(i)

