import sys
import csv
from tabulate import tabulate

def main():
    if len(sys.argv) == 1:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    file_name = sys.argv[1]
    if file_name[-4:] == '.csv':
        try:
            with open(file_name,'r') as f:
                reader = csv.DictRead(f)
                filename = reader[]


            print(n)
        except FileNotFoundError:
            sys.exit("File does not exist")
    else:
        sys.exit("Not a CSV file")
