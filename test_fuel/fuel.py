#!/usr/bin/python3

def main():
    while True:
        try:
            user_input = input('Frection: ')
            percentage = convert(user_input)
            print(gauge(percentage))
        except Exception:
            print('__________')


def convert(fraction):
    try:
        X = int(fraction.replace(' ', '').split('/')[0])
        Y = int(fraction.replace(' ', '').split('/')[1])

        if Y == 0:
            raise ZeroDivisionError("Y cannot be 0")
        if X > Y:
            raise ValueError('X is greater than Y')

        return float(X) / float(Y) * 100

    except Exception as e:
        print('Error:', e)


def gauge(percentage):
    if percentage <= 1:
        return 'E'
    elif percentage >= 99:
        return 'F'
    else:
        return f'{int(percentage + 0.5)}%'


if __name__ == "__main__":
    main()

