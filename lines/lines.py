import sys

if len(sys.argv) == 1:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
file_name = sys.argv[1]
if file_name[-3:] == '.py':
    try:
        with open(file_name,'r') as f:
            lines = f.readlines()
        print(len(lines))
    except FileNotFoundError:
        sys.exit("File does not exist")
else:
    sys.exit("Not a Python file")
