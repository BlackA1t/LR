print('Введите координаты вершины: ')
x1=int(input())
y1=int(input())
print('Введите координаты противоположной вершины: ')
x2=int(input())
y2=int(input())
s1=x2-x1+1
s2=y2-y1+1
p=(s1+s2)*2
s=s1*s2
print('Площадь = ',s,'Периметр = ',p)
