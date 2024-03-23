#!/usr/bin/python3

def main():
    try:
        user_input = input('Greeting: ')
        print('$' + str(value(user_input)))
    except Exception:
        exit(0)


def value(greeting):
    greeting = greeting.replace(' ', '').lower()
    if greeting.startswith('hello'):
        return 0
    elif greeting.startswith('h'):
        return 20
    else:
        return 100


if __name__ == '__main__':
    main()
