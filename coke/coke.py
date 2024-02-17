#!/usr/bin/python3

price = 50
while price > 0:
    print('Amount Due:', price)
    coin = 0
    try:
        coin = int(input('Insert Coin: '))
        if coin in [25, 10, 5]:
            price -= coin
    except:
        pass

print('Change Owed:', - price)
