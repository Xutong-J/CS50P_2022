import requests
import sys

if len(sys.argv) == 1:
    sys.exit("Missing command-line argument")

try:
    n = float(sys.argv[1])

except (ValueError, requests.RequestException):
    sys.exit("Command-line argument is not a number")
    r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    data = r.json()
