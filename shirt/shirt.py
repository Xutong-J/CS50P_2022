from PIL import Image
import sys

def main():
    if len(sys.argv) == 1:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    file_name, out_name = sys.argv[1], sys.argv[2]
    if file_name[-4:] == '.csv':
        try:
            read_write(file_name,out_name)
        except FileNotFoundError:
            sys.exit(f"Could not read {file_name}")
    else:
        sys.exit("Not a CSV file")
