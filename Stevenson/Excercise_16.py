import math

r = int(input("Введите значение радиуса: "))
area = math.pi * r**2
volume = (4/3) * math.pi * (r**2)

print(f'Площадь круга = {"%.2f" % area}')
print(f'Радиус окружности = {"%.2f" % volume}')
