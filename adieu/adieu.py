#!/usr/bin/python3

names = list()
try:
    while True:
        user_input = input('Name: ')
        names.append(user_input)
except EOFError:
    if len(names) < 2:
        print('Adieu, adieu, to ' + names[0])
    elif len(names) == 2:
        print('Adieu, adieu, to ' + names[0] + ' and ' + names[1])
    else:
        print('Adieu, adieu, to ' + ', '.join(names[:-1]) + ', and ' + names[-1])
