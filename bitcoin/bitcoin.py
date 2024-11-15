import requests
import sys

if len(sys.argv) == 1:
    sys.exit("Missing command-line argument")

try:
    n = float(sys.argv[1])
    
except ValueError:
    sys.exit("Command-line argument is not a number")


try:
    ...
except requests.RequestException:
    ...
