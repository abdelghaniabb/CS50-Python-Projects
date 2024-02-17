#!/usr/bin/python3

user_input = input('What is the Answer to the Great Question of Life, the Universe and Everything? ')
new_str = user_input.lower().replace(' ', '')
if new_str in ['42', 'forty-two', 'fortytwo']:
    print('Yes')
else:
    print('No')
