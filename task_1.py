# Функция принимающая 1 аргмент - год и возвращающая True, если год високосный, и Falce иначе

def is_year_leap(year):
    if year % 4 == 0:
        return 'True'
    return 'False'

print(is_year_leap(int(input('Введите год: '))))

# Изменения
