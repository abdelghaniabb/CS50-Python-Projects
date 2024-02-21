#!/usr/bin/python3

def main():
    """this is the main function"""
    while True:
        user_input = input('Date: ')
        if '/' not in user_input:
            try:
                long_date_format(user_input)
            except Exception as e:
                print(e)
        else:
            try:
                short_date_format(user_input)
            except Exception as e:
                print(e)


def long_date_format(s):
    """prints the numeric date format"""
    months = {
        "January": 1,
        "February": 2,
        "March": 3,
        "April": 4,
        "May": 5,
        "June": 6,
        "July": 7,
        "August": 8,
        "September": 9,
        "October": 10,
        "November": 11,
        "December": 12
    }

    s = s.split(' ')
    month = int(months[s[0].title()])
    if ',' not in s[1]:
        return 0
    day = int(s[1].replace(',', ''))
    if day > 31:
        return 0
    print('{}-{:02d}-{:02d}'.format(s[2], month, day))
    exit()


def short_date_format(s):
    """prints the numeric date format"""
    s = s.replace(' ', '').split('/')
    month = int(s[0])
    day = int(s[1])
    if month > 12 or day > 31:
        return 0
    print('{}-{:02d}-{:02d}'.format(s[2], month, day))
    exit()


if __name__ == '__main__':
    main()
