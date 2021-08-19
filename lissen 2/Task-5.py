goods = [57.8, 46.513, 97, 130, 20.14, 30.318, 40.05, 50.98, 200, 321, 334, 82.81]
for good in goods:
    rub = int(good)
    kk = (good - int(good)) * 100
    print(f'{rub} руб {kk:02.0f} коп')
