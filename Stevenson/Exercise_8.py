souve = 75
bauble = 112

vol_souve = int(input("Введите количество сувениров: "))
vol_bauble = int(input("Ведите количество безделушек: "))
sum = (vol_bauble*bauble) + (vol_souve*souve)
print(f"Общий вес посылки:", sum)
