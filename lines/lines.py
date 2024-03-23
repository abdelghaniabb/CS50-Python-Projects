#!/usr/bin/python3

import sys

if len(sys.argv) < 2:
    sys.exit('Too few command-line arguments')
if len(sys.argv) > 2:
    sys.exit('Too many command-line arguments')

if sys.argv[1].split('.')[-1] != 'py':
    sys.exit('Not a Python file')

try:
    f = open(sys.argv[1], 'r')
except FileNotFoundError:
    sys.exit('File does not exist')

count = 0
for line in f:
    new = line.replace(' ', '').replace('\t', '').replace('\n', '')
    if new.startswith('#'):
        pass
    elif new == '':
        pass
    else:
        count += 1

print(count)
