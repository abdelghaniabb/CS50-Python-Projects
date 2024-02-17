#!/usr/bin/python3

user_input = input('Greeting: ')
new_str = user_input.replace(' ', '').lower()

if new_str[0:5] == 'hello':
    print('$0')
elif new_str[0] == 'h':
    print('$20')
else:
    print('$100')

print(new_str[0:4])
