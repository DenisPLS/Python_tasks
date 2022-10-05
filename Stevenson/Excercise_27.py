year = int(input("Введите год: "))
a = year % 19
b = year // 100
c = year % 100
d = b // 4
e = b % 4
f = (b+8) // 25
g = (b-f+1) // 3
h = (19*a+b-d-g+15) % 30
i = c // 4
k = c % 4
l = (32+2*e+2*i-h-k) % 7
m = (a+11*h+22*l) // 451
month = (h+l+7*m+114) // 31
day = 1 + ((h+1-7*m+114) % 31)
if month == 1:
    month = 'Январь'
elif month == 2:
    month = 'Февраль'
elif month == 3:
    month = 'Март'
elif month == 4:
    month = 'Апрель'


print(f'Пасха в {year} году была {day} {month}')
