day = int(input("Введите день месяца: "))
month = input("Введите месяц: ")

if day == 1 and month == 'январь':
    result = 'Новый год'
elif day == 1 and month == 'июль':
    result = 'День Канады'
elif day == 25 and month == 'декабрь':
    result = 'Рождество'
else:
    result = 'На данную дату праздников нет'

print(result)
