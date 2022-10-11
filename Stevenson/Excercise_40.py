vol_sound = int(input("Введите уровень шума в дБ: "))

if vol_sound == 40:
    print("Тихая комната")
elif vol_sound == 70:
    print("Будильник")
elif vol_sound == 106:
    print("Газовая газонокосилка")
elif vol_sound == 130:
    print("Отбойный молоток")
elif 40 < vol_sound < 70:
    print("Уровень шума между Тихой комнатой и Будильником")
elif 70 < vol_sound < 106:
    print("Уровень шума между Будильником и Газонокосилкой")
elif 106 < vol_sound < 130:
    print("Уровень шума между Газонокосилкой и Отбойным молотком")
elif vol_sound < 40:
    print("Значение меньше минимального")
else:
    print("Значение больше максимального")
