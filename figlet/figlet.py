#!/usr/bin/python3

from pyfiglet import Figlet
from sys import argv
import sys

if len(argv) < 2:
    f = Figlet()
if len(argv) == 3 and argv[1] in ['-f', '--font']:
    f = Figlet(font=argv[2])
else:
    sys.exit('USAGE: python figlet.py -f/--font font_name')


user_input = input('Input: ')
print(argv)
print('Output:')
print( f.renderText(user_input))

