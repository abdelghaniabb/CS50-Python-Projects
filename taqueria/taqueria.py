#!/usr/bin/python3

data = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

cost = 0
try:
    while True:
        user_input = input('Item: ')

        if user_input.title()  not in list(data.keys()):
            continue
        cost += data[user_input.title()]
        print(f'Total: ${cost:.2f}')
except EOFError:
    exit()
