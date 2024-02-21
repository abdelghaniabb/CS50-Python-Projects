#!/usr/bin/python3

import random


def main():
    level = get_level()

    array = list()
    for i in range(10):
        array.append((generate_integer(level), generate_integer(level)))
    
    score = 0
    for x, y in array:
        score += get_answer(x, y)

    print('Score: {}'.format(score))


def get_level():
    while True:
        try:
            n = int(input('Level: '))
            if n not in [1, 2, 3]:
                continue
            return n
        except ValueError:
            continue


def generate_integer(level):
    if level > 1:
        mi = int('1' + '0' * (level - 1))
    else:
        mi = 0
    ma = int('9' * level)
    return random.randint(mi, ma)


def get_answer(x, y):
    for i in range(3):
        try:
            answer = int(input('{} + {} = '.format(x, y)))
            if answer == x + y:
                return 1
            else:
                print('EEE')
        except ValueError:
            pass

    print('{} + {} = {}'.format(x, y, x + y))
    return 0


if __name__ == "__main__":
    main()
