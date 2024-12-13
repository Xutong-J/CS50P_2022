import requests
import sys
import json

if len(sys.argv) == 1:
    sys.exit("Missing command-line argument")

try:
    n = float(sys.argv[1])
    r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    data = r.json()
#    print(json.dumps(data))
    bpi = data["bpi"]
    usd = bpi["USD"]
    rate = usd["rate_float"]
    print(f"${rate * n:,.4f}")
except (ValueError, requests.RequestException):
    sys.exit("Command-line argument is not a number")


