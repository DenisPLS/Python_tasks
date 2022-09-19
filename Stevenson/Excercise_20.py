pressure = float(input("Введите давление газа в Па: "))
volume = float(input("Введите объем газа в литрах: "))
temp_c = float(input("Введите температуру в Цельсиях: "))
volume = 0.001 * volume     # Перевод объема газа в метры кубические

r = 8.314
temp_k = temp_c + 273.15        # Температура в Кельвинах
n = (pressure*volume) / (r*temp_k)

print(f'Количество газа равно {"%.2f" % n} моль')
