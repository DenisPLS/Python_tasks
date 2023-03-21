dol = int(input("Введите номинал банкноты: "))

if dol == 1:
    result = 'Джордж Вашингтон'
elif dol == 2:
    result = 'Томас Джефферсон'
elif dol == 5:
    result = 'Авраам Линкольн'
elif dol ==10:
    result = 'Александр Гамильтон'
elif dol == 20:
    result = 'Эндрю Джексон'
elif dol == 50:
    result = 'Улисс Грант'
else:
    result = 'Бенджамин Франклин'

print(result)
