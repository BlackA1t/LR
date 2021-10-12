import math
print('Введите координаты первой вершины: ')
x1=int(input())
y1=int(input())
print('Введите координаты второй вершины: ')
x2=int(input())
y2=int(input())
print('Введите координаты третьей вершины: ')
x3=int(input())
y3=int(input())
s1=math.sqrt((x2-x1)**2+(y2-y1)**2)
s2=math.sqrt((x3-x2)**2+(y3-y2)**2)
s3=math.sqrt((x3-x1)**2+(y3-y1)**2)
p=s1+s2+s3
pp=p/2
s=math.sqrt(pp*(pp-s1)*(pp-s2)*(pp-s3))
print('Площадь = ','%.2f' % s,'Периметр = ','%.2f' % p)
