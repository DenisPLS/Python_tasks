number = int(input("Введите число: "))
numbers = number % 2
if numbers == 0:
    print(f'Число {number} четное')
else:
    print(f'Число {number} нечетное')
