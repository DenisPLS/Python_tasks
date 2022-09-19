import math

radius = float(input("Ввведите радиус цилиндра: "))
height  = float(input("Введите высоту цилиндра: "))

s_circle = math.pi * radius
s_cylinder = s_circle * height

print(f'Площадь цилиндра равна {"%.1f" % s_cylinder}')
