# Найдите сумму всех чисел меньше 1000, кратных 3 или 5.

y = 0
for i in range(1, 1001):
    if i % 3 == 0 or i % 5 == 0:
        y += i
        
print(y)
