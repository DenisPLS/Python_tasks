distance = int(input("Ведите расстояние в футах "))

distance_inch = distance * 12
distance_yd = distance * 0.3333
distance_mi = distance * 0.000189394

print(f'Дистанция в дюймах = {distance_inch}')
print(f'Дистанция в ярдах = {"%.2f" % distance_yd}')
print(f'Дистанция в миллях = {"%.2f" % distance_mi}')
