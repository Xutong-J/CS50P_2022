import sys

if len(sys.argv) == 1:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("TToo many command-line arguments")
file_name = sys.argv[1]
if file_name[-3:] == '.py'


