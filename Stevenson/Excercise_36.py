age_human = int(input("Введите возраст человека: "))
two_years = 10.5
years = 4

if (0<age_human<2):
    age_dog = age_human*two_years
    print(f'Возраст в собачем эквиваленте {age_dog} лет')
elif (1<age_human<3):
    age_dog = age_human * two_years
    print(f'Возраст в собачем эквиваленте {age_dog} лет')
elif age_human <= 0:
    print("Недопустимый возраст")
else:
    age = age_human-2
    age_dog = (two_years*2) + (age*4)
    print(f'Возраст в собачем экваленте {age_dog} лет')
