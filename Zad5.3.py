print('Введите точку А:')
a=int(input())
print('Введите точку C (C между A и B):')
c=int(input())
print('Введите точку B:')
b=int(input())
ac=c-a+1
bc=b-c+1
print('Произведение отрезков АС и ВС = ',ac*bc)
