height_cm = int(input("Введите рост в сантиметрах: "))

ft = 30.48
inch = 2.54
height_ft = height_cm // ft
height_cm = height_cm % ft
height_inch = height_cm / inch
print(f"Ваш рост равен {height_ft} футов {round(height_inch, 2)} дюймов")
