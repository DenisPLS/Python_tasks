month = input("Введите месяц: ")

day = 30

if month == 'Январь' or month == 'Март' or month == 'Май' or month == 'Июль' or month == 'Август' or \
        month == 'Октябрь' or month == 'Декабрь':
    day = 31
elif month == 'Февраль':
    day = "28 или 29"

print(f"В {month} ровно {day} дней")
