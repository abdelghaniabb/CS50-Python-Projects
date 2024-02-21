#!/usr/bin/python3

import random

n = None
while True:
    try:
        n = int(input('Level: '))
        break
    except ValueError:
        pass

goal = random.randint(0, n)
while True:
    try:
        guess = int(input('Guess: '))
    except ValueError:
        pass

    if guess < 0:
        pass
    if guess < goal:
        print('Too small!')
    elif guess > goal:
        print('Too large!')
    else:
        print('Just right!')
        exit()
