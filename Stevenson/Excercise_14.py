height_ft = int(input("Введите рост в футах: "))
height_inch = float(input("Введите рост в дюймах: "))

height_cm = (height_ft*30.48) + (height_inch*2.54)
print(f"Ваш рост равен {round(height_cm)} см.")
