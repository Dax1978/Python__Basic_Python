price = [57.8, 46.51, 97, 57.5, 100.1, 99, 1.12, 33.3, 54.3, 77.07]

def printPrice(p):
    rub = int(p)
    cop = (str(round((p - rub) * 100)), "0" + str(round((p - rub) * 100)))[len(str(round((p - rub) * 100))) < 2]
    print(f"{rub} руб. {cop} коп.")

print('Вывод сортированного по возрастанию списка цен:')
for p in sorted(price):
    printPrice(p)

print('Вывод сортированного по убыванию списка 5 самых высоких цен:')
priceR = sorted(price)[::-1]
for p in priceR [0:5]:
    printPrice(p)