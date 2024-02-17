#!/usr/bin/python3

user_input = input('Expression: ')
expression = user_input.split(' ')
number1 = float(expression[0])
operator = expression[1]
number2 = float(expression[2])

if operator == '+':
    print(number1 + number2)
elif operator == '-':
    print(number1 - number2)
elif operator == '*':
    print(number1 * number2)
elif operator == '/' and number2 != 0:
    print(number1 / number2)
