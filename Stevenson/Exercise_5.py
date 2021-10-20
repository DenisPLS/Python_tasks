bootle_1_liter = int(input("Введите кол-во бутылок объемом 1 литр: "))
bootle_2_liter = int(input("Введите кол-во бутылок большего объема: "))

summa = bootle_1_liter*0.10 + bootle_2_liter*0.25
print("Сумма за бутылки: $%.2f" % summa)
