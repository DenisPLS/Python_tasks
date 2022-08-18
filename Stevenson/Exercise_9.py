sum_depo = int(input("Введите сумму желаемого депозита: "))

i = 2
while i >= 0:
    sum_depo += sum_depo * 0.04
    i -= 1
    print("%.2f" % sum_depo)
