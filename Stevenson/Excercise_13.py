rub_per_ten = 10
rub_per_five = 5
rub_per_two = 2
rub_per_one = 1

sum = int(input("Введите сумму для сдачи: "))

print(" ", sum // rub_per_ten, "десяти рублевых монет")
sum = sum % rub_per_ten
print(" ", sum // rub_per_five, "пяти рублевых монет")
sum = sum % rub_per_five
print(" ", sum // rub_per_two, "двух рублевых монет")
sum = sum % rub_per_two
print(" ", sum // rub_per_one, "одна рублевых монет")
sum = sum % rub_per_one
print(" ", sum, "рублей")
