TAX = 0.18
TIPS = 0.15

order_price = int(input("Введите сумму заказа: "))
tax = order_price * TAX
tips = order_price * TIPS
total = order_price + tax + tips

print("Налог: %.2f" % tax)
print("Чаевые: %.2f" % tips)
print("Итог: %.2f" % total)
