#!/usr/bin/python3

while True:
    user_input = input('Frection: ')
    try:
        number1 = float(user_input.replace(' ', '').split('/')[0])
        number2 = float(user_input.replace(' ', '').split('/')[1])

        if number1 > number2:
            continue

        value = number1 / number2 * 100
        if value <= 1:
            print('E')
        elif value >= 99:
            print('F')
        else:
            print(f'{int(value + 0.5)}%')
        exit()
        
    except Exception as e:
        pass
    
    

