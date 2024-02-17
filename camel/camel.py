#!/usr/bin/python3

user_input = input('camelCase: ')
new_str = ''
for char in user_input:
    if char.isupper():
        new_str += '_' + char.lower()
    else:
        new_str += char

print(new_str)
