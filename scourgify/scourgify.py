import csv
import sys

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
            sys.exit("Could not read {file_name[1]}")
    else:
        sys.exit("Not a CSV file")
