#!/usr/bin/python3

def main():
    value = convert(input('What time is it? '))
    if value >= 7 and value <= 8:
        print('breakfast time')
    elif value >= 12 and value <= 13:
        print('lunch time')
    elif value >= 18 and value <= 19:
        print('dinner time')


def convert(time):
    h = float(time.split(':')[0])
    m = float(time.split(':')[1]) / 60.0
    return h + m


if __name__ == "__main__":
    main()
