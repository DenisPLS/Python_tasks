from math import *

t1 = int(input("Введите широту первой точки: "))
g1 = int(input("Введите долготу первой точки: "))
t2 = int(input("Введите широту второй точки: "))
g2 = int(input("Введите долготу второй точки: "))
distance = 6371.01 * acos(sin(radians(t1)) * sin(radians(t2)) + cos(radians(t1)) * cos(radians(t2))
                          * cos(radians(g1) - radians(g2)))
print(distance)
