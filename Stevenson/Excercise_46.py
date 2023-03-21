cell = input('Введите название клетки (например a1): ')

cell_letter = cell[0]
cell_number = int(cell[1])

if (cell_letter == 'a' or cell_letter == 'c' or cell_letter == 'e' or cell_letter == 'g') and (cell_number == 1 or cell_number == 3 or cell_number == 5 or cell_number == 7):
    result = 'черная'
else:
    result = 'белая'

print(result)
