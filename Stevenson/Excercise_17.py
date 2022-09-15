WATER_HEAT_CAPACITY = 4.186
ELECTRICITY_PRICE = 4.86
J_TO_KWH = 2.777e-7

m = float(input("Введите количество воды в мл: "))
temp_1 = float(input("Введите начальную температуру: "))
temp_2 = float(input("Ведите конечную температуру: "))

q = m * WATER_HEAT_CAPACITY * (temp_2-temp_1)
kwh = q * J_TO_KWH
heatign_price = ELECTRICITY_PRICE * kwh

print(f'Общее количество энергии = {q} Дж')
print(f'Стоимость нагрева {"%.0f" % m} мл. воды  = {"%.2f" % heatign_price} рублей')
