#!/usr/bin/python3

import requests
import sys

if len(sys.argv) < 2:
    sys.exit('Missing command-line argument ')
try:
    n = float(sys.argv[1])
except ValueError:
    sys.exit('Command-line argument is not a number')


try:
    info = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json').json()
    rate = info['bpi']['USD']['rate_float']
except requests.RequestException:
    pass

print('${:,.4f}'.format(n * rate))
