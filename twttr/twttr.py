#!/usr/bin/python3

user_input = input('Input: ')
new_str = ''
for char in user_input:
    if char.lower() not in ['a', 'e', 'i', 'o', 'u']:
        new_str += char

print('Output:', new_str)
