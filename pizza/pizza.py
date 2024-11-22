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
            method2(file_name)
        except FileNotFoundError:
            sys.exit("File does not exist")
    else:
        sys.exit("Not a CSV file")


def method1(file_name):
    list = []
    with open(file_name,'r') as f:
        for line in f:
            row = line.rstrip().split(",")
            list.append(row)
        print(tabulate(list, headers="firstrow", tablefmt="grid"))

def method2(file_name):
    with open(file_name,'r') as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        print(tabulate(rows, headers="keys", tablefmt="grid"))

if __name__ == "__main__":
    main()
