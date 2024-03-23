#!/usr/bin/python3

import sys
import csv
from tabulate import tabulate

if len(sys.argv) < 2:
    sys.exit('Too few command-line arguments')

if len(sys.argv) > 2:
    sys.exit('Too many command-line arguments')

if sys.argv[1].split('.')[-1] != 'csv':
    sys.exit('Not a CSV file')

data = dict()

with open(sys.argv[1], 'r') as infile:
    csv_reader = csv.DictReader(infile)

    for row in csv_reader:
        for key in list(row.keys()):
            data[key] = list()
        break


with open(sys.argv[1], 'r') as infile:
    csv_reader = csv.DictReader(infile)

    for row in csv_reader:
        for key, val in row.items():
            data[key].append(val)



print(tabulate(data, headers='keys', tablefmt='grid'))
