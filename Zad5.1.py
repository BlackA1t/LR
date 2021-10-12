import math
print('Введите координаты первой точки: ')
x1=int(input())
y1=int(input())
print('Введите координаты второй точки: ')
x2=int(input())
y2=int(input())
rast=math.sqrt((x2-x1)**2+(y2-y1)**2)
print('Расстояние между этими точками: ','%.2f' % rast)