#!/usr/bin/python3

import sys
import csv

if len(sys.argv) < 3:
    sys.exit('Too few command-line arguments')

if len(sys.argv) > 3:
    sys.exit('Too many command-line arguments')


fields = ['first', 'last', 'house']
data = list()


try:
    with open(sys.argv[1], 'r') as infile:
        csv_reader = csv.DictReader(infile)

        for row in csv_reader:
            dict_row = dict()
            dict_row['first'] = row['name'].split(',')[0]
            dict_row['last'] = row['name'].replace(' ','').split(',')[1]
            dict_row['house'] = row['house']
            data.append(dict_row)

except FileNotFoundError:
    sys.exit('Could not read {}'.format(sys.argv[1]))


with open(sys.argv[2], 'w', newline='') as outfile:
    writer = csv.DictWriter(outfile, fieldnames=fields)
    writer.writeheader()
    writer.writerows(data)
