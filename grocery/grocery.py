#!/usr/bin/python3

grocery = dict()
try:
    while True:
        user_input = input()
        user_input = user_input.lower()

        if user_input in list(grocery.keys()):
            grocery[user_input] += 1
        else:
            grocery[user_input] = 1

except EOFError:
    keys = list(grocery.keys())
    keys.sort()
    for key in keys:
        print(grocery[key], key.upper())
